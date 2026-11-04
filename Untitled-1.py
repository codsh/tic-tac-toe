def get_winner(position):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in lines:
        if position[a] != '-' and position[a] == position[b] == position[c]:
            return position[a]

    return None


def get_symmetries(position):
    result = []

    for reflected in (False, True):
        for rotation in range(4):
            new_position = ['-'] * 9

            for row in range(3):
                for col in range(3):
                    r, c = row, col

                    if reflected:
                        c = 2 - c

                    for _ in range(rotation):
                        r, c = c, 2 - r

                    new_position[r * 3 + c] = position[row * 3 + col]

            result.append(''.join(new_position))

    return result


def canonical_position(position):
    return min(get_symmetries(position))


def generate_positions():
    positions = set()

    def generate(position, sign):
        positions.add(canonical_position(position))

        if get_winner(position) or '-' not in position:
            return

        for index in range(9):
            if position[index] != '-':
                continue

            new_position = (
                position[:index] + sign + position[index + 1:]
            )

            next_sign = 'O' if sign == 'X' else 'X'
            generate(new_position, next_sign)

    generate('---------', 'X')

    return positions


def ends_in_one_move(position):
    sign = 'X' if position.count('X') == position.count('O') else 'O'

    for index in range(9):
        if position[index] != '-':
            continue

        new_position = (
            position[:index] + sign + position[index + 1:]
        )

        if get_winner(new_position) or '-' not in new_position:
            return True

    return False


positions = generate_positions()

terminal_positions = {
    position for position in positions
    if get_winner(position) or '-' not in position
}

one_move_positions = {
    position for position in positions
    if position not in terminal_positions
    and ends_in_one_move(position)
}

remaining_positions = (
    positions - terminal_positions - one_move_positions
)

print('Всего позиций:', len(positions))
print('Завершённых:', len(terminal_positions))
print('Завершающихся за 1 ход:', len(one_move_positions))
print('Осталось:', len(remaining_positions))

for position in sorted(remaining_positions):
    print(position)