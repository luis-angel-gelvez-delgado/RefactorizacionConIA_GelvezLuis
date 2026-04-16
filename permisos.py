from validaciones import validar_menu

CONTRASENIA_ADMIN = 'admin123'
CONTRASENIA_RESIDENTE = 'residente123'


def _validar_credenciales_admin():
    """Valida las credenciales del administrador."""
    print("-" * 15)
    print("[ZONA DE ACCESO RESTRINGIDO: ADMIN]")
    print("-" * 15)
    contrasenia = input('Introduce la clave de seguridad para continuar: ')
    if contrasenia == CONTRASENIA_ADMIN:
        return 'admin'
    print('Contraseña incorrecta. Serás regresado al menú de ingreso.')
    return None


def _validar_credenciales_residente():
    """Valida las credenciales del residente."""
    print("-" * 15)
    print("[ ÁREA DE RESIDENTES: MI HOGAR ]")
    print("-" * 15)
    contrasenia = input('Introduce la clave de seguridad de residente: ')
    if contrasenia == CONTRASENIA_RESIDENTE:
        return 'residente'
    print('Contraseña incorrecta. Serás regresado al menú de ingreso.')
    return None


def login():
    """Gestiona el inicio de sesión del usuario."""
    while True:
        op = validar_menu('''
            ******************************************
            * *
            * SISTEMA DE INICIO DE SESIÓN *
            * "Tu Amigo del Vecindario" *
            * *
            ******************************************
                    [  ◢◤  SEGURIDAD  ◥◣  ]

            Por favor, identifícate para continuar:

                1. Ingresar como ADMINISTRADOR
                2. Ingresar como RESIDENTE
                3. SALIR DEL SISTEMA

            ------------------------------------------
            >>> Selecciona tu perfil (1-3): ''', 1, 3)
        
        match op:
            case 1:
                resultado = _validar_credenciales_admin()
                if resultado:
                    return resultado
            case 2:
                resultado = _validar_credenciales_residente()
                if resultado:
                    return resultado
            case 3:
                print('''
                    __________________________________________
                    /                                          \\
                    |    👋 ¡HASTA LUEGO, VECINO!              |
                    |__________________________________________/
                    
                    La sesión se ha cerrado correctamente.
                    Gracias por cuidar de nuestra comunidad.
                    
                    [ ESTADO: SISTEMA FUERA DE LÍNEA ]
                    __________________________________________
                    ''')
                break
