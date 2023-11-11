import random
from random import randint, choice


def fill_file_random_number(file_name: str, rows: int):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(rows):
            int_num = random.randint(-1_000, 1_000)
            float_num = random.uniform(-1_000, 1_000)
            line = f'{int_num} | {float_num}\n'
            f.write(line)


def get_random_name():
    min_ord = ord('a')
    max_ord = ord('z')
    min_len = 4
    max_len = 7

    vowel_letters = set('aoueiy')
    len_name = randint(min_len, max_len)
    name = [chr(randint(min_ord, max_ord)) for i in range(len_name)]
    if len(vowel_letters.intersection(set(name))) == 0:
        name[randint(0, len(name) - 1)] = choice(list(vowel_letters))
    name = ''.join(name)
    result = name.capitalize()

    return result


def name_add_mult_numbers(file_1: str, file_2: str):
    with (
        open(file_1, 'r', encoding='utf-8') as num, \
            open(file_2, 'r', encoding='utf-8') as name, \
            open('3.txt', 'w', encoding='utf-8') as res
    ):
        line_1 = num.readlines()
        line_2 = name.readlines()
        max_lines = max(len(line_1), len(line_2))

        for i in range(max_lines):
            l_1 = line_1[i % len(line_1)].strip()
            l_2 = line_2[i % len(line_2)].strip()

            n_1, n_2 = l_1.split(' | ')
            n_1_int = int(n_1)
            n_2_float = float(n_2)

            if n_1_int * n_2_float < 0:
                l_2_lower = l_2.lower()
                result = abs(n_1_int * n_2_float)
                res.write(f'{l_2_lower} | {result}\n')
            else:
                l_2_upper = l_2.upper()
                result = round(n_1_int * n_2_float)
                res.write(f'{l_2_upper} | {result}\n')
