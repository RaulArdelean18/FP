from datetime import datetime

def converteste_string_in_data(data_str):
    """
    Converteste un string 'zi/luna/an' intr-un obiect datetime.
    """

    try:
        parti = data_str.split('/')
        zi = int(parti[0])
        luna = int(parti[1])
        an = int(parti[2])
        return datetime(an, luna, zi)
    except (ValueError, IndexError):
        return None

def format_data_manual(data_obiect):
    """
    Modifica obiect datetime intr-un string 'zi/luna/an'.
    """
    return f"{data_obiect.day}/{data_obiect.month}/{data_obiect.year}"
