import os
from Usuario import usuario,Estudiante,Profesor
from OpcSistema import OpcSistema
from Roles import Rol

class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        print()
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

nom=usuario()
r=Rol()


opc = ""
while opc != "4":
    os.system("cls")
    
    men = Menu("Como desea Ingresar?:",["1)Administrador","2)Estudiante","3)Docente","4)Salir"])
    opc = men.menu()
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 
    if opc == "1":
        opc1 = ""
        os.system("cls")
        print(":::::::::::::ADMINISTRADOR:::::::::::::")
        clave=nom.CUsuarioA()
        nom.MostrarAdmin()
        var=nom.IngresoAdmin()
        opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
        opciones.Mostrar()
        Elementos=""
        while Elementos != clave:
            Elementos = (input("Clave de Admin: "))
            if Elementos==clave:
                input("Clave exitosa Puede ingresar:::::")
                
                
        while opc1 != "6":
                os.system("cls")
                op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                op.Mostrar()
                
                men1 = Menu("Administrador Ingreso a Sistema",["1)Añadir usuario","2)Mostrar", "3)Eliminar", "4)Añadir Nota","5)Buscar","6)Salir"])
                opc1 = men1.menu()

                if opc1 == "1":
                    os.system("cls")
                    opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
                    opciones.Mostrar()
                    print(":::::::::AÑADIR USUARIO DOCENTE:::::::::")
                    nombre=nom.registra()
                    cedula=nom.registraCed()
                    telefono=nom.registraNum()
                    materia=input("Ingrese materia:")
                    carrera=input("Ingrese Carrera:")
                    prof=Profesor(1,nombre,cedula,telefono,materia,carrera)
                    input("Usuario registrado")
                
                    input("Presione una tecla para continuar...")

                elif opc1 == "2":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print(":::::::::AÑADIR USUARIO ESTUDIANTE:::::::::")
                    print()
                    nombre=nom.registra()
                    cedula=nom.registraCed()
                    materia=input("Ingrese materia:")
                    calificacion=input("Ingrese Calificacion de {}:".format(materia))
                    Asistencia=input("Ingrese Asistencia de {}:".format(nombre))
                    estu=Estudiante(2,nombre,cedula,materia,calificacion,Asistencia)
                    input("Usuario registrado")
                    input("Presione una tecla para continuar...")

                elif opc1 == "3":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print("<---Eliminar--->")
                    dato = input(" Digite su dato a Eliminar:")
                    res= resultados.Admineliminar(dato)
                    if res== None:
                        print("Su dato ingresado no esta en la Lista, No se puede eliminar.")
                    else:
                        for pos,ele in enumerate(res):
                            # se guarda el valor eliminado del return
                            if pos==0:
                                num=ele
                            # se guarda la lista del return
                            elif pos==1:
                                num2=ele
                        print("Su Dato:{} se eliminó, Su nueva Lista es:{}".format(num,num2))
                    
                    input("Presione una tecla para continuar...") 
                
                elif opc1 == "4":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print("::::::--Añadir Nota--::::::")
                    dato = (input("Ingrese el dato:"))
                    res=resultados.Adminañadir2(dato)
                    Usu.AñadirDic2()
                    if res:
                        print("El Dato esta ingresado")
                    else:
                        print("La lista esta llena")
                    input("Presione una tecla para continuar...")  

                elif opc1 == "5":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print("<---Buscar--->")
                    dato=input("Ingrese dato a buscar: ")
                    res=resultados.AdminBuscar(dato)
                    if res != -1:
                        print("El elemento {}, esta en la posicion [{}].".format(dato,res))
                    else:
                        print("No se encuentra en la lista...")
                    
                    input("Presione una tecla para continuar...")              
        
        
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    if opc == "2":
        opc1 = ""
        os.system("cls")
        print(":::::::::::::ESTUDIANTE:::::::::::::")
        clave=estu.CUsuarioE()
        var=estu.IngresoEstudiante()
        opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
        opciones.Mostrar()
        Elementos=""
        while Elementos != clave:
            Elementos = (input("Clave de Estudiante: "))
            if Elementos==clave:
                input("Clave exitosa Puede ingresar:::::") 
        input("enter")
        
        while opc1 != "4":
                os.system("cls")
                opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
                opciones.Mostrar()
                men1 = Menu("Estudiantes",["1)Mis Notas","2)Mis Calificaiones","3)Mis Docentes","4)Salir"])
                opc1 = men1.menu()

                if opc1 == "1":
                    os.system("cls")
                    opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
                    opciones.Mostrar()
                    print("::::::::::::MIS NOTAS::::::::::::")
                    print()
                    estu.mostrarNotas()
                    
                    input("Presione una tecla para continuar...")

                elif opc1 == "2":
                    os.system("cls")
                    opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
                    opciones.Mostrar()
                    print("::::::::::::MIS MATERIAS::::::::::::")
                    print()
                    estu.mostrar()
                    
                    input("Presione una tecla para continuar...")

                elif opc1 == "3":
                    os.system("cls")
                    opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
                    opciones.Mostrar()
                    print("::::::::::::MIS DOCENTES::::::::::::")
                    print()
                    prof.mostrarDocente()
                
                    input("Presione una tecla para continuar...")
                    
                    
      
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
         
    if opc == "3":
        opc1 = ""
        os.system("cls")
        print(":::::::::::::DOCENTE:::::::::::::")
        clave=prof.CUsuarioD()
        var=prof.IngresoDocente()
        opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
        opciones.Mostrar()
        Elementos=""
        while Elementos != clave:
            Elementos = (input("Clave de Docente: "))
            if Elementos==clave:
                input("Clave exitosa Puede ingresar:::::") 
        input("enter")
        
        while opc1 != "4":
            
            os.system("cls")
            opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
            opciones.Mostrar()
            men1 = Menu("Menu Docente",["1)Mostrar Calificaciones","2)Mis Materias","3)Mis alumnos","4)Salir"])
            opc1 = men1.menu()
            
            if opc1 == "1":
                os.system("cls")
                opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
                opciones.Mostrar()
                print("{:5}{}".format("",":::::::::Calificaciones de las materias de los Estudiantes:::::::::"))
                print()
                estu.mostrarNotas()
                input("Presione una tecla para continuar...")
                
            elif opc1 == "2":
                os.system("cls")
                opciones=OpcSistema(var,"periodo Julio-2022","Sistema de seguridad SGA")
                opciones.Mostrar()
                print("{:5}{}".format("",":::::::::Mis Materias:::::::::"))
                prof.mostrarDocente()
                print()
                input("Presione una tecla para continuar...")
                
            elif opc1 == "3":
                os.system("cls")
                op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                op.Mostrar()
                print("{:5}{}".format("","<--- Mis Alumnos --->"))
                print()
                estu.mostrar()
                input("Presione una tecla para continuar...")
                                       
    elif opc == "4":
        print("Gracias por usar el sistema")
    else:
        print("Opcion no valida")

    print("Lo espermos en una proxima ocasión")


       
    
    