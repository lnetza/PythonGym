
titularCuenta = "Juan Perez"
saldoCuenta = 100000
contraseñaCuenta = "coco1818"

print("""
    _  _  _  _          _       _           _ _           _    
   (_)(_)(_)(_) _     _(_)_    (_) _       (_|_)       _ (_)   
    (_)        (_)  _(_) (_)_  (_)(_)_     (_|_)    _ (_)      
    (_) _  _  _(_)_(_)     (_)_(_)  (_)_   (_|_) _ (_)         
    (_)(_)(_)(_)_(_) _  _  _ (_|_)    (_)_ (_|_)(_) _          
    (_)        (_|_)(_)(_)(_)(_|_)      (_)(_|_)   (_) _       
    (_)_  _  _ (_|_)         (_|_)         (_|_)      (_) _    
   (_)(_)(_)(_)  (_)         (_|_)         (_|_)         (_)   

""")

while True:
    print("Presiona A PARA OBTENER EL SALDO")
    print("Presiona B PARA DEPOSITAR DINERO")
    print("Presiona C PARA RETIRAR DINERO")
    print("Presiona D PARA VER INFORMACION DE LA CUENTA")
    print("Presiona Q PARA SALIR")

    operacion = input("¿Qué operación deseas realizar? ").lower()

    if operacion == 'a':
        print("SALDO DE LA CUENTA")
        passwordUsuario = input("Ingresa la contraseña de tu cuenta:")
        if passwordUsuario == contraseñaCuenta:
            
            print(f"El saldo de la cuenta es: {saldoCuenta}, pesos")
            print("""
                        ___             ___  
            < - - - - -()_ \< - - - - -()_ \ 
                    !!   | |        !!   | | 
            --------------------------------- 
            """)
        else:
            print("Contraseña incorrecta")
            print("""
            _      _      _    
            oo\    oo\    oo\   
            (__)\  (__)\  (__)\  
            ---------------------- 

            """)
    
    elif operacion == 'b':
        print("DEPOSITO DE DINERO")
        passwordUsuario = input("Ingresa la contraseña de tu cuenta:")
        if passwordUsuario == contraseñaCuenta:
            deposito = int(input("¿Cuánto dinero deseas depositar? "))
            saldoCuenta += deposito
            print(f"Has depositado {deposito} pesos. El nuevo saldo es: {saldoCuenta} pesos.")
            print("""
                        ___             ___  
            < - - - - -()_ \< - - - - -()_ \ 
                    !!   | |        !!   | | 
            --------------------------------- 
            """)
        else:
            print("Contraseña incorrecta")
            print("""
            _      _      _    
            oo\    oo\    oo\   
            (__)\  (__)\  (__)\  
            ---------------------- 

            """)
    elif operacion == 'c':
        print("RETIRAR DINERO")
        passwordUsuario = input("Ingresa la contraseña de tu cuenta:")
        if passwordUsuario == contraseñaCuenta:
            retiro = int(input("¿Cuánto dinero deaseas retirar?"))
            if retiro > saldoCuenta:
                print("Saldo insuficiente en la cuenta")
                print("""
                _      _      _    
                oo\    oo\    oo\   
                (__)\  (__)\  (__)\  
                ---------------------- 

                """)
            else:
                saldoCuenta -= retiro
                print(f"Se ha retirado: {retiro} pesos. Tu saldo actual es: {saldoCuenta} pesos.")
                print("""
                        ___             ___  
            < - - - - -()_ \< - - - - -()_ \ 
                    !!   | |        !!   | | 
            --------------------------------- 
            """)
        else:
            print("Contraseña incorrecta")
            print("""
            _      _      _    
            oo\    oo\    oo\   
            (__)\  (__)\  (__)\  
            ----------------------""")

    elif operacion == 'd':
        print("INFORMACION DE LA CUENTA")
        print("""
            _       _       _       _       _       _    
        _( )__  _( )__  _( )__  _( )__  _( )__  _( )__ 
        _|     _||     _||     _||     _||     _||     _|
        (_ C _ ((_ U _ ((_ E _ ((_ N _ ((_ T _ ((_ A _ (_ 
        |_( )__||_( )__||_( )__||_( )__||_( )__||_( )__| 

        """)
        print(f"Titular de la cuenta:{titularCuenta}")
        print(f"Saldo de la cuenta: {saldoCuenta} pesos")
    elif operacion == 'q':
        print("Gracias por usar el sistema. ¡Hasta luego!")
        print("""   
            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
           ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀            
        """)
        break