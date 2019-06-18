def crear_memoria1(filas,columns,memoria1):
    # creacion del cuadro
    for i in range(filas):
        row1 = []
        for j in range(columns):
            if (j == 0 or i == 0 or i == filas - 1 or j == columns - 1):
                row1.append(".")
            else:
                row1.append(" ")
        memoria1.append(row1)