"""Research model of MikuFlick2 1.1.5. Not an emulator or device test.

No game files, original source code, or assets are bundled. Numeric rules were
recovered by static analysis; scheduling, rendering, replay and BTL are omitted.
"""
import argparse
import json
import math
import struct

FRONT = (5, 5, 5, 4, 4, 4, 4, 3, 3, 2, 2)
BACK = (5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 2, 2)
WEIGHTS = (0, -10, -5, 0, 2, 2)
BASE = (0, 0, 30, 50, 150, 300)
NAMES = ('NONE', 'WORST', 'SAD', 'SAFE', 'FINE', 'COOL')


def f32(x):
    return struct.unpack('<f', struct.pack('<f', x))[0]


def endpoint(offset):
    """Touch clock minus JustFrame; negative means early; integer ticks."""
    table = FRONT if offset <= 0 else BACK
    index = abs(offset)
    return table[index] if index < len(table) else 0


def judge(down, up, board_correct=True, direction_correct=True):
    """One already selected active ordinary note, before BTL adjustments."""
    if not board_correct:
        return 2
    a, b = endpoint(down), endpoint(up)
    result = 0
    if a and b:
        result = min(a, b)
        if result < 3 and down < 0:
            result = 3
    elif not a and down < 0:
        result = min(b, 3)
    return min(result, 5 if direction_correct else 3)


def combo_bonus(combo_after_hit):
    if not isinstance(combo_after_hit, int) or combo_after_hit < 1:
        raise ValueError('combo must be a positive integer')
    # Preserve the recovered ushort truncation before the 500 cap.
    return min(500, (50 * ((combo_after_hit + 5) // 10)) & 0xffff)


def rank(total, cool, fine, safe, game_over=False):
    if total <= 0 or min(cool, fine, safe) < 0 or cool + fine + safe > total:
        raise ValueError('invalid counts')
    if game_over:
        return 'E'
    clear_ratio = f32(f32(cool + fine + safe) / f32(total))
    if clear_ratio < f32(.7):
        return 'D'
    if cool >= total:
        return 'Perfect'
    success_ratio = f32(f32(cool + fine) / f32(total))
    return ('S' if success_ratio >= 1 else 'A' if success_ratio >= f32(.95)
            else 'B' if success_ratio >= f32(.8) else 'C')


def gauge_update(gauge, total, result, sad_already_recorded, worst_already_recorded):
    """Counts at function entry; caller determines current-result inclusion.

    Intended for this sample's ordinary chart lengths (<32768). The native
    failure-count path contains signed-short conversions at higher counts.
    """
    if not 0 < total < 32768 or not 0 <= result <= 5:
        raise ValueError('outside modeled native range')
    step = f32(f32(f32(128.0) / f32(total + total)) + f32(.01))
    new_gauge = min(f32(256), f32(f32(gauge) + f32(step * WEIGHTS[result])))
    ratio = f32(f32(total - sad_already_recorded - worst_already_recorded) / f32(total))
    game_over = new_gauge <= 0 or ratio < f32(.5)
    return (f32(0) if game_over else new_gauge), game_over


def self_test():
    fixtures = [
        (judge(-2, 3), 5), (judge(-3, 0), 4), (judge(0, 4), 4),
        (judge(0, 8), 3), (judge(10, 11), 2), (judge(-9, 10), 3),
        (judge(-11, 0), 3), (judge(12, 12), 0),
        (judge(0, 0, direction_correct=False), 3),
        (judge(0, 0, board_correct=False), 2),
        (rank(100, 100, 0, 0), 'Perfect'), (rank(100, 0, 100, 0), 'S'),
        (rank(100, 95, 0, 5), 'A'), (rank(100, 80, 0, 20), 'B'),
        (rank(100, 0, 0, 70), 'C'), (rank(100, 0, 0, 69), 'D'),
        (rank(100, 100, 0, 0, True), 'E'),
        (combo_bonus(4), 0), (combo_bonus(5), 50), (combo_bonus(14), 50),
        (combo_bonus(15), 100), (combo_bonus(95), 500), (combo_bonus(100), 500),
        (sum(combo_bonus(k) for k in range(1, 101)), 25500),
        (gauge_update(128, 100, 3, 50, 0)[1], False),
        (gauge_update(128, 100, 3, 51, 0)[1], True),
        (gauge_update(1, 100, 1, 0, 1)[1], True),
        (gauge_update(128, 100, 3, 0, 0)[0], 128.0),
        (combo_bonus(13105), 14),
    ]
    for actual, expected in fixtures:
        assert actual == expected, (actual, expected)
    return len(fixtures)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--down', type=int, default=0)
    parser.add_argument('--up', type=int, default=0)
    parser.add_argument('--combo', type=int, default=1)
    parser.add_argument('--wrong-board', action='store_true')
    parser.add_argument('--wrong-direction', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps({'fixture_checks_passed': self_test(), 'device_test': False}))
        return
    result = judge(args.down, args.up, not args.wrong_board, not args.wrong_direction)
    eligible = result >= 4 and not args.wrong_board and not args.wrong_direction
    print(json.dumps({'judgement': NAMES[result], 'base_score': BASE[result],
                      'combo_bonus': combo_bonus(args.combo) if eligible else 0,
                      'scope': 'selected ordinary note; no lifecycle/BTL/replay'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
