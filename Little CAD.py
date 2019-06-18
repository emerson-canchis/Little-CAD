cuadro = []
memoria1 = []
memoria2 = []
memoria3 = []
filas = 42
columns = 82
import f_cuadro
f_cuadro.crear_cuadro(filas,columns,cuadro)
import f_memoria1
f_memoria1.crear_memoria1(filas,columns,memoria1)
import f_memoria2
f_memoria2.crear_memoria2(filas,columns,memoria2)
import f_memoria3
f_memoria3.crear_memoria3(filas,columns,memoria3)
import f_menu
f_menu.menu(filas,columns,cuadro,memoria1,memoria2,memoria3)