def crear_cuadro(filas,columns,cuadro):
    # creacion del cuadro
    for i in range(filas):
        row = []
        for j in range(columns):
            if (j == 0 or i == 0 or i == filas - 1 or j == columns - 1):
                row.append(".")
            else:
                row.append(" ")
        cuadro.append(row)
