first_list = [21, 22, 23, 24, 25, 26]

if len(first_list) % 2 == 0:
    result_list = [first_list[:len(first_list)//2], first_list[len(first_list)//2:]]
else:
    result_list = [first_list[:len(first_list)//2 + 1], first_list[len(first_list)//2 + 1:]]

print(result_list)
second_lists = [
    [21, 22, 23, 24, 25, 26],
    [21, 22, 23],
    [21, 22, 23, 24, 25],
    [21],
    []
]

for first_list in second_lists:
    if len(first_list) % 2 == 0:
        result_list = [first_list[:len(first_list) // 2], first_list[len(first_list) // 2:]]
    else:
        result_list = [first_list[:len(first_list) // 2 + 1], first_list[len(first_list) // 2 + 1:]]

    print(f'{first_list} => {result_list}')
