import random
import re


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def passwords_parameters():
    """длина и количество паролей, пользовательский ввод"""
    numbers = ''
    while numbers == '' or numbers <= 0:
        try:
            numbers = int(input('Количество паролей для генерации: '))
            if numbers <= 0 or numbers > 1000:
                print('Количество паролей для генерации должно быть больше нуля, но не больше 1000')

        except ValueError:
            print('Количество паролей для генерации должно указываться цифрой')
            continue
    length = ''
    while length == '' or length < 6:
        try:
            length = int(input('Длина одного пароля: '))
            if length < 6 or length > 1000:
                print('Длина пароля должна быть больше 6, но не больше 1000')
        except ValueError:
            print('Длину пароля нужно указать цифрой')
            continue

    return numbers, length


def accept_char():
    """задаем допустимые в пароле символы"""

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''

    with_digit = input('Включать ли цифры 0123456789? Enter/n: ')
    with_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Enter/n: ')
    with_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Enter/n: ')
    with_symbols = input('Включать ли символы !#$%&*+-=?@^_? Enter/n: ')

    chars += (digits if with_digit == '' else '')
    chars += (uppercase_letters if with_upper == '' else '')
    chars += (lowercase_letters if with_lower == '' else '')
    chars += (punctuation if with_symbols == '' else '')

    if chars != '':
        no_twice_char = input('Исключать ли неоднозначные символы il1Lo0O? Enter/n: ')
        # удаляем ненужные символы из строки с помощью модуля re.sub и регулярного выражения '[i|l|1|L|o|0|O]'
        chars = (re.sub('[i|l|1|L|o|0|O]', '', chars) if no_twice_char == '' else '')
    return chars


def gen_password(numbers, length, chars_set):
    """генерирование пароля"""
    passwords = []
    for i in range(numbers):
        new_pass = ''
        for j in range(length):
            new_pass += random.choice(chars_set)
        passwords.append(new_pass)
    return passwords


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('this program generates list of passwords on user\'s criteria')
    pass_numbers, pass_len = passwords_parameters()
    # print(pass_numbers, pass_len)
    print()
    print('Теперь определим из каких символов будет состоять пароль ')
    chars_set = ''
    while chars_set == '':
        chars_set = accept_char()
        if chars_set == '':
            print('Не задано ни одного критерия для генерации паролей. Попробуйте')
    print(chars_set)
    print(*gen_password(pass_numbers, pass_len, chars_set), sep='\n')
