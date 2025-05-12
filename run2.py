import sys

import collections

# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]


def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]


def get_key_position(data: list, char):
    position = {}
    for i in data:
        for key in i:
            if key in char:
                position.update({key: [data.index(i), i.index(key)]})
    return position


def get_robot_position(data):
    robots = {}
    r_name = 1
    for indx_l, line in enumerate(data):
        for indx_itm, itm in enumerate(line):
            if itm == '@':
                robots.update({'r' + str(r_name): [[indx_l, indx_itm]]})
                r_name += 1
    return robots


def next_step(data, key, prew_key, keys_char):
    positions = [[+0, -1], [+0, +1], [+1, +0], [-1, +0]]
    for position in positions:
        step = [a + b for a, b in zip(key, position)]
        if data[step[0]][step[1]] in keys_char:
            return data[step[0]][step[1]]

        elif data[step[0]][step[1]] == '.':
            if prew_key:
                if step != prew_key:
                    return step


def solve(data):
    steps = 0
    robot_position = get_robot_position(data)
    key_position = get_key_position(data, keys_char)
    door_position = get_key_position(data, doors_char)

    while key_position:
        for k, v in robot_position.items():
            if len(v) > 1:
                robot_go = next_step(data, v[-1], v[-2], keys_char)
            else:
                robot_go = next_step(data, v[-1], v[-1], keys_char)

            if type(robot_go) == list:
                v.append(robot_go)

            elif robot_go in keys_char:
                v.append(key_position[robot_go])
                data[key_position[robot_go][0]][key_position[robot_go][1]] = '@'
                data[v[0][0]][v[0][1]] = '.'
                robot_position[k] = key_position[robot_go]
                if robot_go.upper() in door_position:
                    data[door_position[robot_go.upper()][0]][door_position[robot_go.upper()][1]] = '.'
                steps += (len(v) - 1)
                robot_position[k] = v[-2:]
                del key_position[robot_go]

    return steps


def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()
