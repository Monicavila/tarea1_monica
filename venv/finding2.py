class Text:
    def __init__(self):
        self.repeated_words = {}
        self.words = []
        self.answer = []

    def manage_txt(self):
        file = input('\n¿Quieres abrir el archivo Clown, Words o Text?:\t')
        file.lower()
        while file.lower() != 'clown' and file.lower() != 'words' and file.lower() != 'text':
            print('Verifica que el nombre sea correcto')
            file = input('\n¿Quieres abrir el archivo Clawn o Words?:\t')
            file.lower()
        file_handler = open(f'{file.strip()}.txt')
        self.words = file_handler.read().split(' ')

    def looking_for(self):
        for word in self.words:
            self.repeated_words[word] = self.repeated_words.get(word, 0) + 1
        print(self.repeated_words)


class Clown(Text):
    def ten_words(self):
        major = 1
        for element in self.repeated_words.values():
            if element > major:
                major = element
                self.answer.append(major)
                major = 1
        words_sorted = (sorted(self.answer, reverse=True))
        for key in self.repeated_words.keys():
            number = words_sorted[0:10]
            if self.repeated_words.get(key) in number:
                print(key, self.repeated_words.get(key))


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