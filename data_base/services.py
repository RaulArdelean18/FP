def adauga_pachet(lista_pachete, destinatie, data_inceput, data_sfarsit, pret):
    """
    Adauga un pachet nou in lista.
    """
    pachet = {
        "destinatie": destinatie,
        "data_inceput": data_inceput,
        "data_sfarsit": data_sfarsit,
        "pret": float(pret)
    }
    lista_pachete.append(pachet)

def modifica_pachet(lista_pachete, index, destinatie_noua, data_inceput_noua, data_sfarsit_noua, pret_nou):
    """
    Modifica un pachet existent la un anumit index.
    """
    lista_pachete[index]["destinatie"] = destinatie_noua
    lista_pachete[index]["data_inceput"] = data_inceput_noua
    lista_pachete[index]["data_sfarsit"] = data_sfarsit_noua
    lista_pachete[index]["pret"] = pret_nou

def pachet_destinatie_pe_pozitie(lista_pachete,index):
    '''

    :param lista_pachete: lista pachetelor
    :param index: pachetul de pe pozitia index in care ne intereseaza destinatia
    :return: desitnatia pachetului index
    '''
    return lista_pachete[index]["destinatie"]

def pachet_pret_pe_pozitie(lista_pachete,index):
    '''

    :param lista_pachete: lista pachetelor
    :param index: pachetul de pe pozitia index in care ne intereseaza pretul
    :return: pretul pachetului index
    '''
    return lista_pachete[index]["pret"]

def pachet_inceput_sejur_pe_pozitie(lista_pachete,index):
    '''

    :param lista_pachete: lista pachetelor
    :param index: pachetul de pe pozitia index in care ne intereseaza inceputul sejurului
    :return: inceputul sejurului pachetului index
    '''
    return lista_pachete[index]["data_inceput"]

def pachet_final_sejur_pe_pozitie(lista_pachete,index):
    '''

    :param lista_pachete: lista pachetelor
    :param index: pachetul de pe pozitia index in care ne intereseaza finalul sejurului
    :return: finalul sejurului pachetului index
    '''
    return lista_pachete[index]["data_sfarsit"]

def sterge_dupa_durata(lista_pachete, durata_minima_zile):
    """
    Returneaza o lista noua eliminand pachetele mai scurte de un numar de zile.
    """
    pachete_pastrate = []
    for pachet in lista_pachete:
        durata_sejur = (pachet['data_sfarsit'] - pachet['data_inceput']).days
        if durata_sejur >= durata_minima_zile:
            pachete_pastrate.append(pachet)
    return pachete_pastrate

def sterge_dupa_destinatie(lista_pachete, destinatie):
    """
    Returneaza o lista noua eliminand pachetele cu destinatia ceruta.
    """
    pachete_pastrate = []
    for pachet in lista_pachete:
        if pachet['destinatie'] != destinatie:
            pachete_pastrate.append(pachet)
    return pachete_pastrate

def sterge_dupa_pret(lista_pachete, pret_maxim):
    """
    Returneaza o lista noua eliminand pachetele cu pretul mai mare decat limita ceruta.
    """
    pachete_pastrate = []
    for pachet in lista_pachete:
        if pachet['pret'] <= pret_maxim:
            pachete_pastrate.append(pachet)
    return pachete_pastrate

def cauta_dupa_interval(lista_pachete, data_inceput_cautare, data_sfarsit_cautare):
    """
    Returneaza pachetele care se incadreaza complet intr-un interval dat.
    """
    rezultat = []
    for pachet in lista_pachete:
        if pachet['data_inceput'] >= data_inceput_cautare and pachet['data_sfarsit'] <= data_sfarsit_cautare:
            rezultat.append(pachet)
    return rezultat

def cauta_dupa_destinatie_si_pret(lista_pachete, destinatie, pret_maxim):
    """
    Returneaza pachetele cu o destinatie data si pret mai mic sau egal decat pret_maxim.
    """
    rezultat = []
    for pachet in lista_pachete:
        if pachet['destinatie'] == destinatie and pachet['pret'] <= pret_maxim:
            rezultat.append(pachet)
    return rezultat

def cauta_dupa_data_sfarsit(lista_pachete, data_sfarsit_cautare):
    """
    Returneaza pachetele care se termina la o data anume.
    """
    rezultat = []
    for pachet in lista_pachete:
        if pachet['data_sfarsit'].date() == data_sfarsit_cautare.date():
            rezultat.append(pachet)
    return rezultat

def filtrare_oferte_dupa_pret_si_destinatie(lista_pachete, destinatie,pret_maxim):
    '''
    Returneaza pachetele care au pret mai mic sau egal decat pret_maxim si nu sunt in destinatia {destinatie}
    :param lista_pachete: lista care cuprinde toate pachetele
    :param destinatie: destinatia in care nu ne dorim sa ajungem
    :param pret_maxim: pretul maxim pe care noi il putem plati pentru un pachet
    :return: o noua lista filtrata cu optiunile noastre
    '''
    rezultat = []

    for pachet in lista_pachete:
        if pachet['pret'] <= pret_maxim and pachet['destinatie'] != destinatie:
                rezultat.append(pachet)

    return rezultat


def filtrare_dupa_luna(lista_pachete, luna):
    """
    Returneaza o lista noua eliminand pachetele care au cel putin o zi in luna specificata.
    """
    pachete_pastrate = []

    for pachet in lista_pachete:
        p_start_luna = pachet['data_inceput'].month
        p_end_luna = pachet['data_sfarsit'].month

        elimina = False

        # Cazul 1: Pachetul incepe sau se termina in luna data
        if p_start_luna == luna or p_end_luna == luna:
            elimina = True

        # Cazul 2: Pachetul se desfasoara in acelasi an si luna e la mijloc
        # (ex: pachet Feb-Apr, luna filtrata = Mar)
        elif p_start_luna < p_end_luna:
            if p_start_luna < luna < p_end_luna:
                elimina = True

        # Cazul 3: Pachetul trece peste ani (ex: pachet Oct -> Feb)
        elif p_start_luna > p_end_luna:
            # Daca luna e in primul an (ex: Oct, Nov, Dec) SAU in al doilea an (ex: Jan, Feb)
            if luna >= p_start_luna or luna <= p_end_luna:
                elimina = True

        # Daca nu trebuie eliminat, il pastram
        if not elimina:
            pachete_pastrate.append(pachet)

    return pachete_pastrate


def raport_perioada_sortat_pret(lista_pachete, data_inceput_cautare, data_sfarsit_cautare):
    """
    Returneaza o lista de pachete dintr-un interval dat, sortata crescator dupa pret.
    Refoloseste logica de la cauta_dupa_interval.
    """

    # 1. Gaseste pachetele din interval (logica deja existenta si testata)
    pachete_gasite = cauta_dupa_interval(lista_pachete, data_inceput_cautare, data_sfarsit_cautare)

    # 2. Sorteaza rezultatele gasite crescator dupa pret
    # Folosim functia 'sorted' pentru a sorta lista dpa cheia 'pret'
    pachete_sortate = sorted(pachete_gasite, key=lambda pachet: pachet['pret'])

    return pachete_sortate