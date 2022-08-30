"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


def revert_rows():
    with open('text.txt') as file:
        with open('revert_text.txt', 'w') as write_file:
            for line in file:
                lst = line.split(' ')
                revert_row = " ".join(lst[::-1])
                write_file.write(revert_row)
    return write_file


revert_rows()
