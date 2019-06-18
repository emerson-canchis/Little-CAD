def menu(filas,columns,memoria1,memoria2,memoria3,cuadro):
    import f_recta
    # menu
    while (True):
        print(
            "\n\t\t MENU:\n1. Agregar una linea\n2. Agregar una elipse o circulo\n3. Agregar un rectangulo o cuadrado\n4. Agregar un triangulo\n5. Mostrar un dibujo\n6. Leer un dibujo\n7. Grabar un dibujo\n\n0. Salir del programa")
        opcion = int(input("Introduzca una opcion: "))
        if (opcion == 0):
            break
        if (opcion == 1):
            print("\n\nHAS ESCOGIDO LA OPCION DE LINEA!\n")
            x_1 = int(input("Introduzca la primera coordenada del primer punto: "))
            y_1 = int(input("Introduzca la segunda coordenada del primer punto: "))
            x_2 = int(input("Introduzca la primera coordenada del segundo punto: "))
            y_2 = int(input("Introduzca la segunda coordenada del segundo punto: "))
            f_recta.recta(x_1, y_1, x_2, y_2,cuadro,filas)
        elif (opcion == 2):
            print("\n\nHAS ESCOGIDO LA OPCION DE ELIPSE O CIRCUNFERENCIA!\n")
            centro_x = int(input("Introduzca el centro(eje X) del circulo o elipse: "))
            centro_y = int(input("Introduzca el centro(eje Y) de la circunferencia o elipse: "))
            radio_x = int(input("Introduzca el radio 1 de la elipse o circunferencia: "))
            radio_y = int(input("Introduzca el radio 2 de la elipse o circunferencia: "))
            for i in range(filas):
                for j in range(columns):
                    # Aproximacion para cubrir mas puntos!
                    if ((((j - centro_x) ** 2) / radio_x ** 2) + (((i - centro_y) ** 2) / (radio_y ** 2)) <= 1.05 and (
                            ((j - centro_x) ** 2) / radio_x ** 2) + (((i - centro_y) ** 2) / (radio_y ** 2)) >= 0.95):
                        cuadro[filas - i][j] = "X"
        elif (opcion == 3):
            print("\n\nHAS ESCOGIDO LA OPCION DE CUADRADO O RECTANGULO\n")
            inf_x = int(input("Ingrese la coordenada X del punto inferior izquierdo: "))
            inf_y = int(input("Ingrese la coordenada Y del punto inferior izquierdo: "))
            base = int(input("Ingrese el tamaño de la base: "))
            altura = int(input("Ingrese la altura: "))
            f_recta.recta(inf_x, inf_y, inf_x + base, inf_y,cuadro,filas)
            f_recta.recta(inf_x, inf_y, inf_x, inf_y + altura,cuadro,filas)
            f_recta.recta(inf_x + base, inf_y, inf_x + base, inf_y + altura,cuadro,filas)
            f_recta.recta(inf_x, inf_y + altura, inf_x + base, inf_y + altura,cuadro,filas)
        elif (opcion == 4):
            print("\n\nHAS SELECCIONADO LA OPCION TRIANGULO!\n")
            inf_x = int(input("Ingrese la coordenada X del punto inferior izquierdo: "))
            inf_y = int(input("Ingrese la coordenada Y del punto inferior izquierdo: "))
            base = int(input("Ingrese el tamaño de la base: "))
            altura = int(input("Ingrese la altura: "))
            f_recta.recta(inf_x, inf_y, inf_x + base, inf_y,cuadro,filas)
            f_recta.recta(inf_x, inf_y, inf_x + int(base / 2), inf_y + altura,cuadro,filas)
            f_recta.recta(inf_x + int(base / 2), inf_y + altura, inf_x + base, inf_y,cuadro,filas)
        elif (opcion == 5):
            for i in range(filas):
                for j in range(columns):
                    print(cuadro[i][j], end="")
                print("")
        elif (opcion == 6):
            print("DIBUJOS GUARDADOS:\n\n1. Memoria 1\n2. Memoria 2\n3. Memoria 3\n")
            dibujo = int(input("\nSeleccione uno de los dibujos guardados: "))
            if (dibujo == 1):
                for i in range(filas):
                    for j in range(columns):
                        cuadro[i][j] = memoria1[i][j]
                for i in range(1, filas - 1):
                    for j in range(1, columns - 1):
                        cuadro[i][j] = ' '
                print("MEMORIA 1 SELECCIONADA!!\n\n")


            elif (dibujo == 2):
                for i in range(filas):
                    for j in range(columns):
                        cuadro[i][j] = memoria2[i][j]
                for i in range(1, filas - 1):
                    for j in range(1, columns - 1):
                        cuadro[i][j] = ' '
                print("MEMORIA 2 SELECCIONADA!!\n\n")
            elif (dibujo == 3):
                for i in range(filas):
                    for j in range(columns):
                        cuadro[i][j] = memoria3[i][j]
                for i in range(1, filas - 1):
                    for j in range(1, columns - 1):
                        cuadro[i][j] = ' '
                print("MEMORIA 3 SELECCIONADA!!\n\n")
        elif (opcion == 7):
            print("\n\nMEMORIAS:\n\n1. Memoria 1\n2. Memoria 2\n3. Memoria 3\n")
            memoria = int(input("SELECCIONE LA MEMORIA DONDE QUIERE GUARDAR SU DIBUJO: "))
            if (memoria == 1):
                for i in range(filas):
                    for j in range(columns):
                        memoria1[i][j] = cuadro[i][j]
                print("MEMORIA 1 SELECCIONADA!!\n\n")

            elif (memoria == 2):
                print("MEMORIA 2 SELECCIONADA!!\n\n")
                for i in range(filas):
                    for j in range(columns):
                        memoria2[i][j] = cuadro[i][j]
            elif (memoria == 3):
                print("MEMORIA 3 SELECCIONADA!!\n\n")
                for i in range(filas):
                    for j in range(columns):
                        memoria3[i][j] = cuadro[i][j]