def recta(x1, y1, x2, y2,cuadro,filas):
    # pendiente inf
    if (x1 == x2):
        for i in range(y1, y2 + 1):
            cuadro[filas - i][x1] = "X"
        return
    # pendiente 0
    if (y1 == y2):
        for i in range(x1, x2 + 1):
            cuadro[filas - y1][i] = "X"
        return
    pendiente = (y2 - y1) / (x2 - x1)
    # aproximacion +-0.05 para obtener mas puntos xd
    if (pendiente > 0):
        for i in range(min(y1 + 1, y2), max(y1 + 1, y2)):
            for j in range(min(x1 + 1, x2), max(x1 + 1, x2)):
                if (x1 - j == 0): continue
                if ((y2 - y1) / (x2 - x1) <= ((y1 - i) / (x1 - j)) + 0.05 and (y2 - y1) / (x2 - x1) >= (
                        (y1 - i) / (x1 - j)) - 0.05):
                    cuadro[filas - i][j] = "X"
    elif (pendiente < 0):
        for i in range(min(y1 + 1, y2), max(y1 + 1, y2)):
            for j in range(max(x1 + 1, x2), min(x1 + 1, x2), -1):
                if (x1 - j == 0): continue
                if ((y2 - y1) / (x2 - x1) <= ((y1 - i) / (x1 - j)) + 0.05 and (y2 - y1) / (x2 - x1) >= (
                        (y1 - i) / (x1 - j)) - 0.05):
                    cuadro[filas - i][j] = "X"