
class Publication:
    def __init__(self, name):
        self.name = name
    def printInfo(self):
        print(f'\nNimi: {self.name}')
        
class Book(Publication):
    def __init__(self, name, author, pageCount):
        self.author = author
        self.pageCount = pageCount
        super().__init__(name)
    def printInfo(self):
        super().printInfo()
        print(f'Kirjoittaja: {self.author}. {self.pageCount} sivua.')
        
class Magazine(Publication):
    def __init__(self, name, chiefEditor):
        self.chiefEditor = chiefEditor
        super().__init__(name)
    def printInfo(self):
        super().printInfo()
        print(f'Päätoimittaja: {self.chiefEditor}')
        
mag1 = Magazine("Aku Ankka", "Aki Hyyppä")
book1 = Book("Hytti n:o 6", "Rosa Liksom", 200)

mag1.printInfo()
book1.printInfo()
        
        