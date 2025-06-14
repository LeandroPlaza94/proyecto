from datetime import datetime

def horario_disponible(clientes, categoria, hora, fecha):
    """
    Verifica si el horario está disponible para la categoría y fecha dadas.
    Retorna True si está disponible, False si está ocupado.
    """
    try:
        hora_turno = datetime.strptime(hora, "%H:%M")
    except ValueError:
        return False  # Formato incorrecto

    for c in clientes:
        if c.get("categoria") == categoria and c.get("fecha") == fecha:
            try:
                hora_existente = datetime.strptime(c.get("hora", ""), "%H:%M")
                if abs((hora_turno - hora_existente).total_seconds()) / 3600 < 1:
                    return False
            except Exception:
                continue
    return True