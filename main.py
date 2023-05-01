from Repo_file.repo_file import Repository_file
from Service.service_masini import Service_masini
from UI.consola import Console


def start():
    repo_start = Repository_file("../../Structuri_date/Lab_1/data/masini.txt")
    service = Service_masini(repo_start)
    consola = Console(service)

    consola.meniu()

start()
