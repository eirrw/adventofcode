with open('input') as file:
    data = file.read().splitlines()

split = data.index("")
orders = data[:split]
updates = data[split+1:]

# print(orders, updates)

rules = {}
for new_rule in orders:
    (page, req) = [int(s) for s in new_rule.split('|')]
    rule = rules.setdefault(page, set())
    rule.add(req)
    rules[page] = rule

# print(rules)

total = 0
for update in updates:
    valid = True
    printed = set()
    update = [int(s) for s in update.split(',')]
    for page in update:
        reqs = rules.setdefault(page, [])
        if any(x in printed for x in reqs):
            valid = False
            break
        printed.add(page)

    if valid:
        mid = update[len(update) // 2]
        total += mid

print(total)
