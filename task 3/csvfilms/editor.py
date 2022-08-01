import csv


class Editor:
    """
    Editor for .csv files.
    Current file information is saved in list items
    (list items is empty after initialisation of class object).
    """

    items = []

    def __init__(self, model, file_name):
        """

        :param model: model of data in .csv file(can be inherited from Item class)
        :type model: Item
        :param file_name: name of .csv file(for example: 'file.csv')
        :type file_name: str
        """
        self.model = model
        self.file_name = file_name

    def read(self):
        new_items = []
        with open(self.file_name, newline='') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i > 0:
                    new_items.append(self.model(*row))
        self.items = new_items

    def add(self, item):
        if not isinstance(item, self.model):
            return False
        with open(self.file_name, 'a', newline='') as file:
            field_names = self.model.fieldnames()
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writerow(item.__dict__)
            self.items.append(item)
        return True

    def remove(self, index):
        self.items.pop(index)
        with open(self.file_name, 'w', newline='') as file:
            field_names = self.model.fieldnames()
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            for item in self.items:
                writer.writerow(item.__dict__)
