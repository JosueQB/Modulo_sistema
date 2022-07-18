class OperacionesPropias():
    def Asistencia(self,alumno="Rolando Josue Quijije Banchon",asistencia="100%"):
        text="Alumno"
        text2="Asistencia"
        print("{:5} {:20} {}".format("",text,text2))
        print("   ***********           ************** ")
        print("{:3} {:20} {}".format("",alumno,asistencia))
    


class OpcSistema():
    def __init__(self,Usuario,periodo,NomEmp):
        self.usuario=Usuario
        self.periodo=periodo
        self.nomemp=NomEmp
        
        
    def Mostrar(self):
        print("")
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("{:35} {:20} {}".format(self.nomemp,self.periodo,self.usuario))
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    
    def MostrarOpc(self,texa="1)ASISTENCIA",desa="Ver asistencia",texm="3)MATERIA",desm="Ver Materias",texc="2)CALIFICACIONES",desc="Ver Calificaion"):
        print("{:5} {:25} {:25} {}".format("",texa,texc,texm))
        print("{:3} {:27} {:23} {}".format("",desa,desc,desm))

    
        
            
        
        
un=OpcSistema("Josue Quijije","Periodo Mayo-2022","SGA")
un.MostrarOpc()
