def crear_memoria2(filas,columns,memoria2):
    # creacion del cuadro
    for i in range(filas):
        row2 = []
        for j in range(columns):
            if (j == 0 or i == 0 or i == filas - 1 or j == columns - 1):
                row2.append(".")
            else:
                row2.append(" ")
        memoria2.append(row2)