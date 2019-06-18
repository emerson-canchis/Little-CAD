def crear_memoria3(filas,columns,memoria3):
    # creacion del cuadro
    for i in range(filas):
        row3 = []
        for j in range(columns):
            if (j == 0 or i == 0 or i == filas - 1 or j == columns - 1):
                row3.append(".")
            else:
                row3.append(" ")
        memoria3.append(row3)