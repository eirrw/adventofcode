total = 0

with open('input', 'r') as fp:
    for line in fp:
        first_num = None
        last_num = None

        for char in line:
            if char.isdigit():
                if first_num is None:
                    first_num = char
                    last_num = char
                else:
                    last_num = char

        full_num = first_num + last_num
        total += int(full_num)


print(total)
