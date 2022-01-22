def func_order(*args):
    key_def = []

    frontier = 1

    while len(set(key_def)) != len(args):
        key_def = [args[i][0:frontier] for i in range(len(args))]
        frontier += 1

    key_def = [str.upper(i) for i in key_def]

    key_def_num = []

    for colloc in key_def:
        a = ''
        for letter in colloc:
            a = a + str(ord(letter))
        key_def_num.append(int(a, 10))

    words_dict = dict(zip(key_def_num, args))

    for i in range(len(key_def_num)):
        for y in range(len(key_def_num)):
            if key_def_num[i] < key_def_num[y]:
                key_def_num[i], key_def_num[y] = key_def_num[y], key_def_num[i]

    return [words_dict[i] for i in key_def_num]


def write_lines_file(filename: str):
    with open(filename, 'w') as f:
        print('Type text by lines.\n\nOnce done press spacebar.\n')
        while (line := f'{input()}\n') != '\n':
            f.write(line)


def count_lines(filename: str):
    from os.path import getsize

    with open(filename, 'r') as f:
        count = 0
        while f.readline() != '':
            count += 1
        return count, getsize(filename)


def ch_pos(a:dict):
    a = {y: x for x, y in a.items()}#notes +
    return a


def shuffle_da_deck(deck:list, times_to_shuffle=10000):
    import random
    n = len(deck)
    for _ in range(times_to_shuffle):
        card1 = random.randint(0, n - 1)
        card2 = random.randint(0, n-1)
        deck[card1], deck[card2] = deck[card2], deck[card1]
    return deck

# print(func_order('Liam', 'Noah', 'Oliver', 'Ava', 'Avvva', 'Swaroop', 'Gleb'))
# write_lines_file('file_file.txt')
# print(count_lines('file_file.txt'))
# l = {str(i - 96):chr(i) for i in range(ord('a'), ord('z'))}
# print(ch_pos(l))
# l = {y: x for x, y in l.items()}#note
# notes = {'C0': '16.35', 'C#0': '17.32', 'D0': '18.35', 'D#0': '19.45', 'E0': '20.60', 'F0': '21.83', 'F#0': '23.12', 'G0': '24.50', 'G#0': '25.96', 'A0': '27.50', 'A#0': '29.14', 'B0': '30.87', 'C1': '32.70', 'C#1': '34.65', 'D1': '36.71', 'D#1': '38.89', 'E1': '41.20', 'F1': '43.65', 'F#1': '46.25', 'G1': '49.00', 'G#1': '51.91', 'A1': '55.00', 'A#1': '58.27', 'B1': '61.74', 'C2': '65.41', 'C#2': '69.30', 'D2': '73.42', 'D#2': '77.78', 'E2': '82.41', 'F2': '87.31', 'F#2': '92.50', 'G2': '98.00', 'G#2': '103.83', 'A2': '110.00', 'A#2': '116.54', 'B2': '123.47', 'C3': '130.81', 'C#3': '138.59', 'D3': '146.83', 'D#3': '155.56', 'E3': '164.81', 'F3': '174.61', 'F#3': '185.00', 'G3': '196.00', 'G#3': '207.65', 'A3': '220.00', 'A#3': '233.08', 'B3': '246.94', 'C4': '261.63', 'C#4': '277.18', 'D4': '293.66', 'D#4': '311.13', 'E4': '329.63', 'F4': '349.23', 'F#4': '369.99', 'G4': '392.00', 'G#4': '415.30', 'A4': '440.00', 'A#4': '466.16', 'B4': '493.88', 'C5': '523.25', 'C#5': '554.37', 'D5': '587.33', 'D#5': '622.25', 'E5': '659.25', 'F5': '698.46', 'F#5': '739.99', 'G5': '783.99', 'G#5': '830.61', 'A5': '880.00', 'A#5': '932.33', 'B5': '987.77', 'C6': '1046.50', 'C#6': '1108.73', 'D6': '1174.66', 'D#6': '1244.51', 'E6': '1318.51', 'F6': '1396.91', 'F#6': '1479.98', 'G6': '1567.98', 'G#6': '1661.22', 'A6': '1760.00', 'A#6': '1864.66', 'B6': '1975.53', 'C7': '2093.00', 'C#7': '2217.46', 'D7': '2349.32', 'D#7': '2489.02', 'E7': '2637.02', 'F7': '2793.83', 'F#7': '2959.96', 'G7': '3135.96', 'G#7': '3322.44', 'A7': '3520.00', 'A#7': '3729.31', 'B7': '3951.07', 'C8': '4186.01', 'C#8': '4434.92', 'D8': '4698.63', 'D#8': '4978.03', 'E8': '5274.04', 'F8': '5587.65', 'F#8': '5919.91', 'G8': '6271.93', 'G#8': '6644.88', 'A8': '7040.00', 'A#8': '7458.62', 'B8': '7902.13'}
# print(ch_pos(notes))
# print(len(notes))
deck52 = [(x, y) for x in ['A','2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K'] for y in ('+', '^', '<>', 'V')]
print(shuffle_da_deck(deck52))
