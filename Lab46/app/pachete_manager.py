def creeaza_manager_stare():
    """
    Creeaza manager pentru starea aplicatiei (pachete).
    :return: dict cu 2 chei: 'lista_curenta' (lista de pachete)
                             'lista_undo' (lista cu starile anterioare)
    """
    return {
        'lista_curenta': [],
        'lista_undo': []
    }

def get_lista_curenta(manager_stare):
    """Returneaza lista curenta de pachete."""
    return manager_stare['lista_curenta']

def get_lista_undo(manager_stare):
    """Returneaza lista de undo."""
    return manager_stare['lista_undo']

def set_lista_curenta(manager_stare, lista_noua):
    """Seteaza lista curenta de pachete."""
    manager_stare['lista_curenta'] = lista_noua

def adauga_la_undo(manager_stare, stare_de_salvat):
    """Adauga o stare (o lista de pachete) in lista de undo."""
    manager_stare['lista_undo'].append(stare_de_salvat)

def pop_din_undo(manager_stare):
    """Scoate ultima stare din lista de undo si o returneaza."""
    return manager_stare['lista_undo'].pop()

def are_stari_undo(manager_stare):
    """Verifica daca mai exista stari in lista de undo."""
    return len(manager_stare['lista_undo']) > 0

def executa_undo(manager_stare):
    """
    Executa operatia de undo.
    Modifica managerul de stare setand lista curenta la starea anterioara.
    :param manager_stare: managerul starii curente
    :return: True daca operatia a reusit, False daca nu mai exista stari de undo.
    """
    if are_stari_undo(manager_stare):
        # Scoatem ultima stare salvata
        lista_anterioara = pop_din_undo(manager_stare)
        # O setam ca fiind starea curenta
        set_lista_curenta(manager_stare, lista_anterioara)
        return True
    else:
        # Nu s-a putut face undo
        return False