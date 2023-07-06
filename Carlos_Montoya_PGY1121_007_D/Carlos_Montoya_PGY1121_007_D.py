import funciones as fn

while True:
    fn.mostrar_menu()
    opc=fn.validar_opc()
    if opc==1:
        fn.comprar()
    elif opc==2:
        fn.mostrar_concierto()
    elif opc==3:
        fn.listado_asistentes()
    elif opc==4:
        fn.ganancias()
    elif opc==5:
        fn.salir()
        break