class Pokemon:
    """
    Класс, который создает покемона с атрибутами имя и тип покемона
    А также переопределяет метод строкового представления объекта
    """

    def __init__(self, name: str, poketype: str):
        """
        конструктор, инициализирующий имя и тип покемона
        """
        self.name = name
        self.poketype = poketype

    def __str__(self) -> str:
        """
        магический метод для определения строкового представления объекта
        """
        return f'{self.name}/{self.poketype}'


if __name__ == '__main__':
    # 1 Pokemon/магический метод
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
