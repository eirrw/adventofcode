from typing import NamedTuple, List
from bisect import bisect_left
import concurrent.futures


class Map(NamedTuple):
    dest: int
    source: int
    range: int


def get_closest(maps: List[Map], idx: int):
    pos = bisect_left(maps, idx, key=lambda m: m.source)
    if pos == 0:
        if maps[0].source == idx:
            return maps[0]
        return None
    elif pos == len(maps):
        return maps[-1]

    if maps[pos].source == idx:
        return maps[pos]

    return maps[pos - 1]


def proc_seeds(seed_start: int, seed_range: int, maps: List[List[Map]]):
    print('Starting thread for seed {} with range {}'.format(seed_start, seed_range))
    loc = None
    for seed in range(seed_start, seed_start + seed_range):
        cur_idx = seed
        for maps in all_maps:
            val = get_closest(maps, cur_idx)
            if val is not None:
                if cur_idx in range(val.source, val.source + val.range):
                    offset = cur_idx - val.source
                    cur_idx = val.dest + offset

        if loc is None:
            loc = cur_idx
        else:
            loc = min(loc, cur_idx)

    return loc


sts_map: List[Map] = []
stf_map: List[Map] = []
ftw_map: List[Map] = []
wtl_map: List[Map] = []
ltt_map: List[Map] = []
tth_map: List[Map] = []
htl_map: List[Map] = []


#with open('example1') as fp:
with open('input') as fp:
    current_map = None
    for line in fp:
        if line.find('seeds:') == 0:
            seeds = [int(i) for i in line.strip().split(' ')[1:]]
            if len(seeds) % 2 != 0:
                exit(128)
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
all_maps = [sts_map, stf_map, ftw_map, wtl_map, ltt_map, tth_map, htl_map]
for maps in all_maps:
    maps.sort(key=lambda item: item.source)

locs = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executer:
    future_to_seed = {executer.submit(proc_seeds, seeds[si], seeds[si+1], all_maps): si for si in range(0, len(seeds), 2)}
    for future in concurrent.futures.as_completed(future_to_seed):
        idx = future_to_seed[future]
        try:
            data = future.result()
            locs.append(data)
        except Exception as exc:
            print('%r generated an exception: %s' % (seeds[idx], exc))
        else:
            print('%r has location %d' % (seeds[idx], data))


print(locs)
print(min(locs))
