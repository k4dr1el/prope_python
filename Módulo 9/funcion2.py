def mission_report(tiempo_lanzamiento, tiempo_vuelo, destino, tanque_respaldo, tanque_principal):
    return f"""
    Mision a {destino}
    tiempo de viaje: {tiempo_lanzamiento + tiempo_vuelo} min
    total de combustible restante: {tanque_respaldo + tanque_principal} lts
    """

print(mission_report(10, 25, "Luna", 40, 50))


def mission_report(destino, *min, **tanque):
    return f"""
    Mision a {destino}
    Tiempo total de viaje: {sum(min)} minutes
    tiempo restante: {sum(tanque.values())}
    """

print(mission_report("Luna", 10, 15, 51, main=34, external=6987))


def mission_report(destino, *min, **tanque):
    main_report = f"""
    Mission a {destino}
    Tiempo total de viaje: {sum(min)} minutes
    tiempo restante: {sum(tanque.values())}
    """
    for tank_name, litros in tanque.items():
        main_report += f"{tank_name} tank --> {litros} lts left\n"
    return main_report

print(mission_report("Marte", 8, 11, 55, main=34, external=567788))