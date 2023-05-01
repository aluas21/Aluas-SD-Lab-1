from Service.service_masini import Service_masini
import time

class Console:
    def __init__(self, service_masini: Service_masini):
        self.service_masini = service_masini

    def print_meniu(self):
        print("1. Afisare lista")
        print("2. Sortare: ")
        print("3. Cautare dupa token: ")

    def print_lista(self):
        print(*self.service_masini.get_All(), sep='\n')

    def print_criterii(self):
        print("Alegeti criteriul ")
        print("1. Sorteaza dupa token")
        print("2. Sorteaza dupa marca si model")
        print("3. Sorteaza dupa marca, model, token")
        print("4. Sorteaza dupa profit")

    def sortare_normala(self):
        self.print_criterii()
        opt = input("Alegeti optiune")
        time_start = time.time()
        if opt == "1":
            print(*self.service_masini.sortare_for_in_for("token"), sep='\n')
        elif opt == "2":
            print(*self.service_masini.sortare_for_in_for("marca", "model", "model"), sep='\n')
        elif opt == "3":
            print(*self.service_masini.sortare_for_in_for("marca", "model", "token"), sep='\n')
        elif opt == "4":
            print(*self.service_masini.sortare_for_in_for("get_profit"), sep='\n')
        print(f"Timpul de executie este de: {time.time() - time_start} secunde")

    def sortare_eficienta(self):
        self.print_criterii()
        lista = list(self.service_masini.get_All())
        st = 0
        dr = len(lista)
        opt = input("Alegeti optiune")
        time_start = time.time()
        if opt == "1":
            self.service_masini.sortare_quick_sort(lista,st,dr-1,"token")
            print(*lista, sep = "\n")
        elif opt == "2":
            self.service_masini.sortare_quick_sort(lista,st,dr-1,"marca", "model", "model")
            print(*lista, sep = "\n")
        elif opt == "3":
            self.service_masini.sortare_quick_sort(lista,st,dr-1,"marca", "model", "token")
            print(*lista, sep = "\n")
        elif opt == "4":
            self.service_masini.sortare_quick_sort(lista,st,dr-1,"get_profit")
            print(*lista, sep = "\n")
        print(f"Timpul de executie este de: {time.time() - time_start} secunde")

    def print_cautare(self):
        token = input("Introduceti token: ")
        print("1. Cautare secventiala")
        print("2. Cautare binara")
        opt = input("Alegeti optiunea")
        time_start = time.time()
        if opt == "1":
            print(self.service_masini.cautare_secventiala(token))
            print(f"Timpul de executie este de: {time.time() - time_start} secunde")
        elif opt == "2":
            lista = list(self.service_masini.get_All())
            st = 0
            dr = len(lista)
            self.service_masini.sortare_quick_sort(lista,st,dr-1,"token")
            print(self.service_masini.cautare_binara(lista,st,dr-1,token))
            print(f"Timpul de executie este de: {time.time() - time_start} secunde")

    def medota_sortare(self):
        print("1. Sortare cu eficienta O(n^2)")
        print("2. Sortare cu eficienta O(nlogn)")
        opt = input("Alegeti metoda de sortare: ")
        if opt == "1":
            self.sortare_normala()
        if opt == "2":
            self.sortare_eficienta()

    def meniu(self):
        #marca_mod_comp = lambda a,b: a if a.marca == b.marca and a.model < b.model else # if a.marca <b.marca else b
        while True:
            self.print_meniu()
            opt = input("Alegeti optiunea")
            if opt == "1":
                self.print_lista()
            elif opt == "2":
                self.medota_sortare()
            elif opt == "3":
                self.print_cautare()
            elif opt == "x":
                break