
class Item:
    """
    Item is an abstract class.
    Classes that inherit class Item can be used as a model for Editor.
    Each attribute of the class is the field name of .csv file.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'item - {self.name}'

    def __repr__(self):
        return f'item - {self.name}'

    @classmethod
    def fieldnames(cls):
        return ['name']
