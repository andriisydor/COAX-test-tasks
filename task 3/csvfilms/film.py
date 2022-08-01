from .item import Item


class Film(Item):
    """
    Class Film can be used as a model for Editor.
    """

    def __init__(self, name, note, rating):
        """

        :param name: film name
        :type name: str
        :param note: film description
        :type note: str
        :param rating: film rating(this field is used for comparing Film class objects)
        :type rating: float
        """

        self.name = name
        self.note = note
        self.rating = float(rating)

    def __str__(self):
        return f'{self.name} -- {self.rating}\n' \
               f'{self.note}'

    def __repr__(self):
        return f'{self.name} - {self.rating} - {self.note}'

    def __lt__(self, other):
        return self.rating < other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __radd__(self, other):
        return other + self.rating

    @classmethod
    def fieldnames(cls):
        return ['name', 'note', 'rating']


def best_top(films, number=5):
    return sorted(films, reverse=True)[:number]


def worst_top(films, number=5):
    return sorted(films)[:number]


def average_rating(films):
    return sum(films) / len(films)
