"""Read recovered tables from a locally owned MikuFlick2 sample; no writes."""
import argparse
import hashlib
import json
from pathlib import Path
import struct

EXPECTED = '869caa22613c5ebfbde6b4c9e1a93362a4f30519231b6dfc9ac3ff31d414b87f'


class MachO:
    def __init__(self, path):
        self.data = Path(path).read_bytes()
        if struct.unpack_from('<I', self.data)[0] != 0xfeedface:
            raise ValueError('expected thin little-endian 32-bit Mach-O')
        self.sha256 = hashlib.sha256(self.data).hexdigest()
        self.segments = []
        self.cryptid = None
        self.cpu_type, self.cpu_subtype = struct.unpack_from('<II', self.data, 4)
        p = 28
        for _ in range(struct.unpack_from('<I', self.data, 16)[0]):
            command, size = struct.unpack_from('<II', self.data, p)
            if size < 8 or p + size > len(self.data):
                raise ValueError('invalid load command')
            if command == 1:
                va, virtual_size, offset, file_size = struct.unpack_from('<4I', self.data, p + 24)
                self.segments.append((va, offset, file_size))
            if command == 0x21:
                self.cryptid = struct.unpack_from('<I', self.data, p + 16)[0]
            p += size

    def read(self, address, length):
        for va, offset, file_size in self.segments:
            if va <= address and address + length <= va + file_size:
                start = offset + address - va
                return self.data[start:start + length]
        raise ValueError('address not file backed: ' + hex(address))

    def unpack(self, address, fmt):
        return list(struct.unpack('<' + fmt, self.read(address, struct.calcsize('<' + fmt))))


def inspect(path):
    m = MachO(path)
    if m.sha256 != EXPECTED:
        raise ValueError('sample hash differs; do not apply these version-specific addresses')
    numeric = {'source_sha256': m.sha256, 'cpu_type': m.cpu_type, 'cpu_subtype': m.cpu_subtype,
               'cryptid': m.cryptid}
    for key, address, count in [
        ('early_at_0x139488', 0x139488, 11), ('late_at_0x1394b4', 0x1394b4, 12),
        ('interlude_early_at_0x13ac6c', 0x13ac6c, 11), ('interlude_late_at_0x13ac98', 0x13ac98, 12),
        ('base_score_at_0x1394e4', 0x1394e4, 12), ('gauge_weights_at_0x138f4c', 0x138f4c, 6),
        ('difficulty_timeout_offsets_at_0x1392fc', 0x1392fc, 5),
        ('telop_dispatch_at_0x140c44', 0x140c44, 6), ('interlude_dispatch_at_0x140c38', 0x140c38, 3),
    ]:
        numeric[key] = m.unpack(address, 'i' * count)
    numeric['rank_thresholds_at_0x4c424'] = m.unpack(0x4c424, 'fff')
    numeric['bpm_140_instruction_hex'] = m.read(0xe5c6, 4).hex()
    numeric['kana_board_table'] = m.unpack(0x13a454, 'i' * 190)
    numeric['kana_direction_table'] = m.unpack(0x13a74c, 'i' * 190)
    numeric['kana_subtype_table'] = m.unpack(0x139c80, 'i' * 190)
    return numeric


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('binary', type=Path)
    p.add_argument('--compare-data', type=Path, help='compare with published numeric_tables.json')
    args = p.parse_args()
    result = inspect(args.binary)
    if args.compare_data:
        reference = json.loads(args.compare_data.read_text())
        shared = sorted(set(reference) & set(result))
        for key in shared:
            if reference[key] != result[key]:
                raise ValueError('table mismatch: ' + key)
        result['published_tables_compared'] = shared
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
