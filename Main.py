from Menu import Menu
if __name__ == '__main__':
    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Registrar un helado vendido
              2 Ver 5 sabores más pedidos
              3 Cantidad de gramos vendidos de un sabor
              4 Mostrar tipos de helado vendidos segun peso""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0