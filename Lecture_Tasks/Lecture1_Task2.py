class EmojiMixin:
    """
    Миксин, добавляющий доп. функциональность классу в виде
    замены типов покемонов в строковом представлении на смайлики
    """

    def swap_poketype(self, poketype: str) -> str:
        """
        метод который принимает на вход тип покемона и меняет его
        на смайлик
        """
        self.swap = {
            'grass': '🌿',
            'fire': '🔥',
            'water': '🌊',
            'electric': '⚡'
        }
        return self.swap[poketype]

    def __str__(self) -> str:
        """
        переопределенный магический метод для определения строкового
        представления объекта дополнительно меняется тип покемона на смайлик
        """
        return f'{self.name}/{self.swap_poketype(self.poketype)}'


class BasePokemon:
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


class Pokemon(EmojiMixin, BasePokemon):
    """
    Класс наследник Pokemon, который наследует функциональность
    двух классов родителей, поэтому не содержит дополнительных
    методов и атрибутов, объявленных внутри
    """
    pass


if __name__ == '__main__':
    # 2 Pokemon/миксин
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
    pikachu = Pokemon(name='Pikachu', poketype='electric')
    print(pikachu)
