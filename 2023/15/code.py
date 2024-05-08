from collections import namedtuple

with open('input') as fp:
    codes = fp.read().strip().split(',')

Lens = namedtuple('Lens', ['label', 'focal_length'])


def do_hash(code):
    val = 0
    for c in code:
        if c == '\n':
            raise RuntimeError

        val += ord(c)
        val *= 17
        val %= 256

    return val


vals = []
for code in codes:
    val = do_hash(code)
    vals.append(val)

print(sum(vals))

boxes: dict[int, list[Lens]] = {}
for code in codes:
    if '-' in code:
        func = code.index('-')
    else:
        func = code.index('=')

    label = code[:func]
    box_id = do_hash(label)

    box = boxes.setdefault(box_id, [])
    if code[func] == '-':
        for k, lens in enumerate(box):
            if lens.label == label:
                box.pop(k)
    elif code[func] == '=':
        slot = len(box)
        for k, lens in enumerate(box):
            if lens.label == label:
                slot = k
                break

        lens = Lens(label, int(code[func+1]))
        if slot == len(box):
            box.append(lens)
        else:
            box[slot] = lens
powers = []
for i, box in zip(boxes.keys(), boxes.values()):
    for slot, lens in enumerate(box):
        boxval = (1 + i)
        slotval = (1 + slot)
        power = (1 + i) * (1 + slot) * lens.focal_length
        # print(f"{lens.label}: {boxval}, {slotval}, {lens.focal_length} = {power}")
        powers.append(power)

# print(powers)
print(sum(powers))
