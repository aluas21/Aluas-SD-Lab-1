from Repo_file.repo_file import Repository_file


class Service_masini:
    def __init__(self, repo_masini : Repository_file):
        self.repo_masini = repo_masini

    def get_All(self):
        return self.repo_masini.get_all()

    def sortare_for_in_for(self, *comparator):
        lista = list(self.repo_masini.get_all())
        for i in range(0, len(lista) - 1):
            for j in range(i+1, len(lista)):
                if lista[i].__getattribute__(comparator[0]) > lista[j].__getattribute__(comparator[0]):
                    lista[i],lista[j] = lista[j], lista[i]
                elif lista[i].__getattribute__(comparator[0]) == lista[j].__getattribute__(comparator[0]):
                     if lista[i].__getattribute__(comparator[1]) > lista[j].__getattribute__(comparator[1]):
                        lista[i], lista[j] = lista[j], lista[i]
                     elif lista[i].__getattribute__(comparator[1]) == lista[j].__getattribute__(comparator[1]):
                        if lista[i].__getattribute__(comparator[2]) > lista[j].__getattribute__(comparator[2]):
                            lista[i], lista[j] = lista[j], lista[i]
        return lista

    def sortare_quick_sort(self, lista, st, dr, *comparator):
        if st < dr:
            m = int((st + dr) / 2)
            lista[st], lista[m] = lista[m], lista[st]
            i = st
            j = dr
            d = 0
            while i < j:
                if lista[i].__getattribute__(comparator[0]) > lista[j].__getattribute__(comparator[0]):
                    lista[i], lista[j] = lista[j], lista[i]
                    d = 1 - d
                elif lista[i].__getattribute__(comparator[0]) == lista[j].__getattribute__(comparator[0]):
                    if lista[i].__getattribute__(comparator[1]) > lista[j].__getattribute__(comparator[1]):
                        lista[i], lista[j] = lista[j], lista[i]
                        d = 1 - d
                    elif lista[i].__getattribute__(comparator[1]) == lista[j].__getattribute__(comparator[1]):
                        if lista[i].__getattribute__(comparator[2]) > lista[j].__getattribute__(comparator[2]):
                            lista[i], lista[j] = lista[j], lista[i]
                            d = 1 - d
                i += d
                j -= 1 - d
            try:
                self.sortare_quick_sort(lista, st, i - 1, comparator[0], comparator[1], comparator[2])
                self.sortare_quick_sort(lista, i + 1, dr, comparator[0], comparator[1], comparator[2])
            except IndexError:
                try:
                    self.sortare_quick_sort(lista, st, i - 1, comparator[0], comparator[1])
                    self.sortare_quick_sort(lista, i + 1, dr, comparator[0], comparator[1])
                except IndexError:
                    self.sortare_quick_sort(lista, st, i - 1, comparator[0])
                    self.sortare_quick_sort(lista, i + 1, dr, comparator[0])

    def cautare_secventiala(self, token):
        for masina in self.repo_masini.get_all():
            if masina.token == token:
                return masina
        return "Nu exista acest token"

    def cautare_binara(self, lista, st, dr, token):
        while st<dr:
            m = int((st+dr)/2)
            if lista[m].token == token:
                return lista[m]
            elif lista[m].token > token:
                dr = m - 1
            elif lista[m].token < token:
                st = m + 1
        return "Nu exista acest token"
