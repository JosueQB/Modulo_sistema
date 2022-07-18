import os
from OpcSistema import OpcSistema
from Usuario import usuario
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
Usu=Rol()


opc = ""
while opc != "4":
    os.system("cls")
    
    men = Menu("Como desea Ingresar?:",["1)Docente","2)Estudiante","3)administrador","4)Salir"])
    opc = men.menu()
# ______________________________________________________________________________________________________________________
    if opc == "1":
        opc1 = ""
        os.system("cls")
        Elementos=""
        while Elementos != "D":
            nom=(input("Ingrese su Usuario:"))
            Elementos = (input("Clave de Docente: "))
            if Elementos=="D":
                resultado = Usu
# ______________________________________________________________________________________________________________________
        while opc1 != "4":
            
            os.system("cls")
            op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
            op.Mostrar()
            men1 = Menu("Menu Docente",["1)Mostrar Calificaciones","2)Mis Materias","3)Mis alumnos","4)Salir"])
            opc1 = men1.menu()
# ______________________________________________________________________________________________________________________
            if opc1 == "1":
                os.system("cls")
                op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                op.Mostrar()
                print("{:5}{}".format("","<--- Calificaciones de las materias de los Estudiantes --->"))
                print()
                resultado.DocenteMostrar()
                input("Presione una tecla para continuar...")
                
            elif opc1 == "2":
                os.system("cls")
                op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                op.Mostrar()
                print("{:5}{}".format("","<--- Mis Materias --->"))
                print()
                resultado.DocenteMat()
                
                input("Presione una tecla para continuar...")
                
            elif opc1 == "3":
                os.system("cls")
                op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                op.Mostrar()
                print("{:5}{}".format("","<--- Mis Alumnos --->"))
                print()
                resultado.DocenteAlumnnos()
                Usu.Adminmostrar()
                input("Presione una tecla para continuar...")
           
# ______________________________________________________________________________________________________________________
    if opc == "2":  

            opc1 = ""
            os.system("cls")
            Elementos=""
            while Elementos != "E":
                nom=(input("Ingrese su Usuario:"))
                Elementos = (input("Clave de Estudiante: "))
                if Elementos=="E":
                    resultado = Usu
# ______________________________________________________________________________________________________________________
            while opc1 != "4":
                os.system("cls")
                op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                op.Mostrar()
                o=op.MostrarOpc()
                men1 = Menu("Estudiantes",[o,"4)Salir"])
                opc1 = men1.menu()
# ______________________________________________________________________________________________________________________
                if opc1 == "1":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print("<---Mostrar Asistencia--->")
                    
                    
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                 
                elif opc1 == "2":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print("<---Mostrar Calificaciones--->")
                    
                    
                    input("Presione una tecla para continuar...")
 # ______________________________________________________________________________________________________________________                       
                elif opc1 == "3":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print("<---Mostrar Materia--->")
                    
                
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                                 
                
    if opc == "3":  

            opc1 = ""
            os.system("cls")
            Elementos=""
            while Elementos != "A":
                nom=(input("Ingrese su Usuario:"))
                Elementos = (input("Clave de Administrador: "))
            if Elementos=="A":
                resultados = Usu
            
# ______________________________________________________________________________________________________________________
            while opc1 != "6":
                os.system("cls")
                op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                op.Mostrar()
                
                men1 = Menu("Administrador Ingreso a Sistema",["1)Añadir","2)Mostrar", "3)Eliminar", "4)Añadir Nota","5)Buscar","6)Salir"])
                opc1 = men1.menu()
# ______________________________________________________________________________________________________________________
                if opc1 == "1":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print("<---Añadir--->")
                    dato = (input("Ingrese el dato:"))
                    res=resultados.Adminañadir(dato)
                    if res:
                        print("El Dato esta ingresado")
                    else:
                        print("La lista esta llena")
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________   
                elif opc1 == "2":
                    os.system("cls")
                    op=OpcSistema(nom,"Periodo Mayo-2022","SGA")
                    op.Mostrar()
                    print("<---Mostrar--->")
                    resultados.Adminmostrar()
                    
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                        
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
# ______________________________________________________________________________________________________________________                            
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
# ______________________________________________________________________________________________________________________                                       
    elif opc == "4":
        print("Gracias por usar el sistema")
    else:
        print("Opcion no valida")

    print("Lo espermos en una proxima ocasión")