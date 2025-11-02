def creeaza_pachet(destinatie, data_inceput, data_sfarsit, pret):
    """
    Creeaza si returneaza un dictionar nou de tip pachet.
    Aceasta este singura functie care stie structura interna a dictionarului.
    """
    return {
        "destinatie": destinatie,
        "data_inceput": data_inceput,
        "data_sfarsit": data_sfarsit,
        "pret": float(pret)
    }


# --- Gettere (pentru a citi datele fara acces direct) ---

def get_destinatie(pachet):
    """Returneaza destinatia unui pachet."""
    return pachet["destinatie"]


def get_pret(pachet):
    """Returneaza pretul unui pachet."""
    return pachet["pret"]


def get_data_inceput(pachet):
    """Returneaza data de inceput a unui pachet."""
    return pachet["data_inceput"]


def get_data_sfarsit(pachet):
    """Returneaza data de sfarsit a unui pachet."""
    return pachet["data_sfarsit"]


def adauga_pachet(lista_pachete, destinatie, data_inceput, data_sfarsit, pret):
    """
    Creeaza un pachet nou si il returneaza intr-o lista noua.
    """
    pachet = creeaza_pachet(destinatie, data_inceput, data_sfarsit, pret)

    # Returneaza o LISTA NOUA care contine pachetele vechi + cel nou
    return lista_pachete + [pachet]

def modifica_pachet(lista_pachete, index, destinatie_noua, data_inceput_noua, data_sfarsit_noua, pret_nou):
    """
    Modifica un pachet existent la un anumit index.
    (Folosesc 'creeaza_pachet' pentru a inlocui pachetul vechi).
    """
    pachet_modificat = creeaza_pachet(destinatie_noua, data_inceput_noua, data_sfarsit_noua, pret_nou)
    # Am creat o lista noua
    lista_noua = []
    for i in range(len(lista_pachete)):
        if i == index:
            # Adauga pachetul modificat la pozitia corecta
            lista_noua.append(pachet_modificat)
        else:
            # Adauga pachetul vechi, nemodificat
            lista_noua.append(lista_pachete[i])

    # Returneaza lista NOUA, nu cea veche
    return lista_noua


def sterge_dupa_durata(lista_pachete, durata_minima_zile):
    """
    Returneaza o lista noua eliminand pachetele mai scurte de un numar de zile.
    """
    pachete_pastrate = []
    for pachet in lista_pachete:
        data_sf = get_data_sfarsit(pachet)
        data_in = get_data_inceput(pachet)

        durata_sejur = (data_sf - data_in).days
        if durata_sejur >= durata_minima_zile:
            pachete_pastrate.append(pachet)
    return pachete_pastrate


def sterge_dupa_destinatie(lista_pachete, destinatie):
    """
    Returneaza o lista noua eliminand pachetele cu destinatia ceruta.
    """
    pachete_pastrate = []
    for pachet in lista_pachete:
        if get_destinatie(pachet) != destinatie:
            pachete_pastrate.append(pachet)
    return pachete_pastrate


def sterge_dupa_pret(lista_pachete, pret_maxim):
    """
    Returneaza o lista noua eliminand pachetele cu pretul mai mare decat limita ceruta.
    """
    pachete_pastrate = []
    for pachet in lista_pachete:
        if get_pret(pachet) <= pret_maxim:
            pachete_pastrate.append(pachet)
    return pachete_pastrate


def cauta_dupa_interval(lista_pachete, data_inceput_cautare, data_sfarsit_cautare):
    """
    Returneaza pachetele care se incadreaza complet intr-un interval dat.
    """
    rezultat = []
    for pachet in lista_pachete:
        if get_data_inceput(pachet) >= data_inceput_cautare and \
                get_data_sfarsit(pachet) <= data_sfarsit_cautare:
            rezultat.append(pachet)
    return rezultat


def cauta_dupa_destinatie_si_pret(lista_pachete, destinatie, pret_maxim):
    """
    Returneaza pachetele cu o destinatie data si pret mai mic sau egal decat pret_maxim.
    """
    rezultat = []
    for pachet in lista_pachete:
        if get_destinatie(pachet) == destinatie and get_pret(pachet) <= pret_maxim:
            rezultat.append(pachet)
    return rezultat


def cauta_dupa_data_sfarsit(lista_pachete, data_sfarsit_cautare):
    """
    Returneaza pachetele care se termina la o data anume.
    """
    rezultat = []
    for pachet in lista_pachete:
        if get_data_sfarsit(pachet).date() == data_sfarsit_cautare.date():
            rezultat.append(pachet)
    return rezultat


def filtrare_oferte_dupa_pret_si_destinatie(lista_pachete, destinatie, pret_maxim):
    """
    Returneaza pachetele care au pret mai mic sau egal decat pret_maxim
    si nu sunt in destinatia {destinatie}.
    """
    rezultat = []
    for pachet in lista_pachete:
        if get_pret(pachet) <= pret_maxim and get_destinatie(pachet) != destinatie:
            rezultat.append(pachet)
    return rezultat


def filtrare_dupa_luna(lista_pachete, luna):
    """
    Returneaza o lista noua eliminand pachetele care au cel putin o zi in luna specificata.
    """
    pachete_pastrate = []
    for pachet in lista_pachete:
        p_start_luna = get_data_inceput(pachet).month
        p_end_luna = get_data_sfarsit(pachet).month

        elimina = False
        if p_start_luna == luna or p_end_luna == luna:
            elimina = True
        elif p_start_luna < p_end_luna:
            if p_start_luna < luna < p_end_luna:
                elimina = True
        elif p_start_luna > p_end_luna:
            if luna >= p_start_luna or luna <= p_end_luna:
                elimina = True

        if not elimina:
            pachete_pastrate.append(pachet)
    return pachete_pastrate


def raport_perioada_sortat_pret(lista_pachete, data_inceput_cautare, data_sfarsit_cautare):
    """
    Returneaza o lista de pachete dintr-un interval dat, sortata crescator dupa pret.
    """
    pachete_gasite = cauta_dupa_interval(lista_pachete, data_inceput_cautare, data_sfarsit_cautare)

    # Folosim getter in lambda
    pachete_sortate = sorted(pachete_gasite, key=lambda pachet: get_pret(pachet))

    return pachete_sortate


def raport_numar_oferte_destinatie(lista_pachete, destinatie):
    """
    Returneaza numarul de oferte pentru o destinatie data.
    """
    count = 0
    for pachet in lista_pachete:
        if get_destinatie(pachet) == destinatie:
            count += 1
    return count


def raport_medie_pret_destinatie(lista_pachete, destinatie):
    """
    Returneaza media pretului pentru o destinatie data.
    Returneaza 0 daca nu exista pachete.
    """
    total_pret = 0
    count = 0
    for pachet in lista_pachete:
        if get_destinatie(pachet) == destinatie:
            total_pret += get_pret(pachet)
            count += 1

    if count == 0:
        return 0
    return total_pret / count