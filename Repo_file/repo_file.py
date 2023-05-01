
from Domain.Entitati import Masina


class Repository_file:
    def __init__(self, file_name):
        self.entitati = {}
        self.file_name = file_name
        self.load_data()

    def get_all(self):
        return self.entitati.values()

    def get_by_id(self, id):
        return self.entitati.get(id, None)

    def load_data(self):
        with open(self.file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                line.replace("\n", "")
                array = line.split()
                self.entitati[array[2]] = Masina((array[0]), array[1], array[2], int(array[3]), int(array[4]))

