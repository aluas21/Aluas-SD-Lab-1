from dataclasses import dataclass


@dataclass
class Masina:
    marca : str
    model : str
    token : str
    pret_achizitionare : int
    pret_vanzare : int

    @property
    def get_profit(self):
        return (self.pret_vanzare - self.pret_achizitionare)

    def __str__(self):
        return f"marca: {self.marca}, model: {self.model}, token masina: {self.token}, pret achizitie: {self.pret_achizitionare}, pret vanzare: {self.pret_vanzare}"

