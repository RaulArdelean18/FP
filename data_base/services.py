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
