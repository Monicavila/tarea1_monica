"""
Source of reference: python.org

--> os
Miscellaneous operating system interfaces
--> os.scandir(path='.')
To expose the file path and other file attributes of a directory entry.
--> is_file(*, follow_symlinks=True)
Return True if this entry is a file or a symbolic link pointing to a file;
return False if the entry is or points to a directory or other non-file entry,
or if it doesn’t exist anymore.

--> operator
Converts calls to various functions in the operator module to other, but equivalent, function calls.
-->operator.itemgetter(item)
Return a callable object that fetches item from its operand using the operand’s __getitem__() method.
Dictionaries accept any hashable value. Lists, tuples, and strings accept an index or a slice.

-->enumerate(iterable, start=0)
Return an enumerate object. Iterable must be a sequence, an iterator, or some other object which
supports iteration.
"""

import os
import operator


class Text:
    def __init__(self):
        self.repeated_words = {}
        self.words = []
        self.answer = []

    def manage_txt(self):
        folder = '/Users/moonita/PycharmProjects/tarea1_monica/venv'
        with os.scandir(folder) as files:
            files = [files.name for files in files if files.is_file()]
        file = input('\n¿Cual archivo extensión *.txt quieres abrir?:\t')
        file.lower()
        if f'{file.lower()}.txt' in files:
            file_handler = open(f'{file.lower().strip()}.txt')
            self.words = file_handler.read().split(' ')

    def looking_for(self):
        for word in self.words:
            self.repeated_words[word] = self.repeated_words.get(word, 0) + 1
        print(self.repeated_words)


class Clown(Text):
    def ten_words(self):
        words_sort = sorted(self.repeated_words.items(), key=operator.itemgetter(1), reverse=True)
        for word in enumerate(words_sort[0:10]):
            print(word[1][0], self.repeated_words[word[1][0]])


class Lorem(Clown):
    pass


text_1 = Clown()
text_1.manage_txt()
text_1.looking_for()
text_1.ten_words()

text_2 = Lorem()
text_2.manage_txt()
text_2.looking_for()
text_2.ten_words()
