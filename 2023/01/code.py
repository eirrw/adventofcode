import re


def proc_num(num: str) -> str:
    if num.isdigit():
        parsed_num = num
    else:
        if num == 'one':
            parsed_num = 1
        elif num == 'two':
            parsed_num = 2
        elif num == 'three':
            parsed_num = 3
        elif num == 'four':
            parsed_num = 4
        elif num == 'five':
            parsed_num = 5
        elif num == 'six':
            parsed_num = 6
        elif num == 'seven':
            parsed_num = 7
        elif num == 'eight':
            parsed_num = 8
        elif num == 'nine':
            parsed_num = 9

    return str(parsed_num)


total = 0
with open('input', 'r') as fp:
    for line in fp:
        first_num = None
        last_num = None

        nums = re.findall(
            "(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))",
            line
        )

#        for char in line:
#            if char.isdigit():
#                if first_num is None:
#                    first_num = char
#                    last_num = char
#                else:
#                    last_num = char

        print(nums)

        first_num = proc_num(nums[0])
        last_num = proc_num(nums[-1])

        full_num = str(first_num) + str(last_num)
        print(full_num)
        total += int(full_num)

print(total)

