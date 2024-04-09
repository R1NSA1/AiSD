class Publication:
    def __init__(self, title, author_lastname):
        self.title = title
        self.author_lastname = author_lastname

    def displayinfo(self):
        pass

    def isrequested(self, author_lastname):
        if self.author_lastname == author_lastname:
            return True
        else:
            return False


class Book(Publication):
    def __init__(self, title, author_lastname, year, publisher):
        super().__init__(title, author_lastname)
        self.year = year
        self.publisher = publisher

    def displayinfo(self):
        print(f'Название книги: "{self.title}"')
        print(f'Автор: {self.author_lastname}')
        print(f'Год публикации: {self.year}')
        print(f'Опубликовал: {self.publisher}')


class Article(Publication):
    def __init__(self, title, author_lastname, journal, issue, year):
        super().__init__(title, author_lastname)
        self.journal = journal
        self.issue = issue
        self.year = year

    def displayinfo(self):
        print(f'Название заголовка: "{self.title}"')
        print(f'Автор: {self.author_lastname}')
        print(f'Журнал: "{self.journal}"')
        print(f'Вопросы: {self.issue}')
        print(f'Год публикации: {self.year}')


class ElectronicResource(Publication):
    def __init__(self, title, author_lastname, link, annotation):
        super().__init__(title, author_lastname)
        self.link = link
        self.annotation = annotation

    def displayinfo(self):
        print(f'Название ресурса: "{self.title}"')
        print(f'Автор: {self.author_lastname}')
        print(f'Ссылка: {self.link}')
        print(f'Аннотация: {self.annotation}')


publications = [Book("Python Programming", "Smith", 2019, "Tech Publishing"),
                Article("Data Analysis Techniques", "Johnson", "Science Journal", 12, 2020),
                ElectronicResource("Machine Learning Basics", "Brown", "www.learnml.com",
                                   "Introduction to ML")]

# Display full information
for publication in publications:
    publication.displayinfo()
    print()

# Search by author last name
print('Введите фамилию автора:')
author_lastname = input(str())
for publication in publications:
    if publication.isrequested(author_lastname):
        print(f'Найдена публикация автора {author_lastname}:')
        print()
        publication.displayinfo()
        break
    else:
        print(f'У автора {author_lastname} не найдены публикации.')
