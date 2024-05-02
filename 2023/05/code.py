from typing import NamedTuple, List


class Map(NamedTuple):
    dest: int
    source: int
    range: int


def get_closest(maps: List[Map], idx: int):
    try:
        return max([i for i in maps if idx >= i.source], key=lambda i: i.source)
    except ValueError:
        return None


sts_map: List[Map] = []
stf_map: List[Map] = []
ftw_map: List[Map] = []
wtl_map: List[Map] = []
ltt_map: List[Map] = []
tth_map: List[Map] = []
htl_map: List[Map] = []


with open('input') as fp:
    current_map = None
    for line in fp:
        if line.find('seeds:') == 0:
            seeds = [int(i) for i in line.strip().split(' ')[1:]]
            continue

        if 'seed-to-soil' in line:
            current_map = sts_map
            continue
        elif 'soil-to-fertilizer' in line:
            current_map = stf_map
            continue
        elif 'fertilizer-to-water' in line:
            current_map = ftw_map
            continue
        elif 'water-to-light' in line:
            current_map = wtl_map
            continue
        elif 'light-to-temperature' in line:
            current_map = ltt_map
            continue
        elif 'temperature-to-humidity' in line:
            current_map = tth_map
            continue
        elif 'humidity-to-location' in line:
            current_map = htl_map
            continue

        if current_map is not None and line.strip() != '':
            data = Map(*[int(i) for i in line.strip().split(' ')])
            current_map.append(data)

for maps in [sts_map, stf_map, ftw_map, wtl_map, ltt_map, tth_map, htl_map]:
    maps.sort(key=lambda item: item.source)

locations = []
for seed in seeds:
    cur_idx = seed
    for maps in [sts_map, stf_map, ftw_map, wtl_map, ltt_map, tth_map, htl_map]:
        # print('current: ', cur_idx)
        val = get_closest(maps, cur_idx)
        if val is not None:
            if cur_idx in range(val.source, val.source + val.range):
                offset = cur_idx - val.source
                cur_idx = val.dest + offset

    locations.append(cur_idx)
    # print('final: ', cur_idx)

print(min(locations))
