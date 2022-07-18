class usuario():
    def __init__(self):
        self.lista=[]
        self.nota=[]
        self.dic={}
        self.usu=[]
        
    def registra(self):
        while True:
            valor = (input("{} ".format("Ingrese Nombres Completos:")))
            if valor.isalpha():
                break
            else:
                print("{}".format("!!!!!!! solo nombres"))
        return valor
    
    def registraCed(self):
        while True:
            valor = (input("{} ".format("Ingrese Cedula:")))
            try:
                if int(valor)>0:
                    break
            except:
                print("{}".format("!!!!!! solo numeros "))
        return valor
    
    def registraNum(self):
        while True:
            valor = (input("{} ".format("Ingrese Numero de contacto:")))
            try:
                if int(valor)>0:
                    break
            except:
                print("{}".format("!!!!!!!solo numeros"))
        return valor
    

    
    def MostrarAdmin(self):
        print("{}{:5}{}".format("ADMIN","","rquijijeb2@unemi.edu.ec"))       
    
    
    def CUsuarioA(self):
        ClaveA="Admin2022"
        return ClaveA
                
    def IngresoAdmin(self,UsuA="Admin"):
        Usu=""
        while Usu != UsuA:
            nom=(input("Ingrese su Usuario:"))
            if nom == UsuA:
                return nom
            else:
                print("Usuario Invalido") 
    
          
    
                       
    

            
class Profesor(): 
    def __init__(self,id2,nomb,cedul,telefon,materi,carrer):
        self.__id = id2
        self.nombre = nomb
        self.cedula = cedul
        self.telefono = telefon
        self.materia = materi
        self.carrera= carrer
    @property
    def id(self):
        return self.__id

    def getProfesor(self):
        return  [str(self.id),self.nombre,self.cedula,self.telefono,self.materia,self.carrera]
    
    def IngresoDocente(self,UsuD="Dvera"):
        Usu=""
        while Usu != UsuD:
            nom=(input("Ingrese su Usuario:"))
            if nom == UsuD:
                return nom  
            else:
                print("Usuario Invalido") 
    def mostrarDocente(self): 
        var=self.getProfesor()
        print("{:4}{:19}{:18}{}".format("","DOCENTE","MATERIA","CARRERA"))
        print("{:5}{:19}{:19}{}".format("",var[1],var[4],var[5]))        
        
        
    def CUsuarioD(self):
        ClaveD="Docente2022"
        return ClaveD
    
    def ingreso(self,clave):
        Elementos=""
        while Elementos != clave:
            Elementos = (input("Clave de Ingreso: "))
            if Elementos==clave:
                print("ingreso")
                
            else:
                print("Clave Invalida")     
                
class Estudiante(): 
    def __init__(self,id,nombre,cedula,materia,calificaiones,Asistencia):
        self.__id = id
        self.nombreE = nombre
        self.cedulaE = cedula
        self.materiaE=materia
        self.cal = calificaiones
        self.asis = Asistencia
        self.lista=[]
    
    @property
    def id(self):
        return self.__id

    def getEstudiante(self):
        return  [str(self.id),self.nombreE,self.cedulaE,self.materiaE,self.cal,self.asis]
    
    
    def CUsuarioE(self):
        ClaveE="Estu2022"
        return ClaveE   
    
        
    def IngresoEstudiante(self,UsuE="rquijije"):
        Usu=""
        while Usu != UsuE:
            nom=(input("Ingrese su Usuario:"))
            if nom == UsuE:
                return nom
            else:
                print("Usuario Invalido") 
                
    def mostrarNotas(self): 
        var=self.getEstudiante()
        print("{:4}{:19}{:18}{}".format("","ESTUDIANTE","NOTA","ASISTENCIA"))
        print("{:5}{:19}{:19}{}".format("",var[1],var[4],var[5]))       
    
    def mostrar(self): 
        var=self.getEstudiante()
        print("{:4}{:19}{}".format("","ESTUDIANTE","MATERIA"))
        print("{:5}{:19}{}".format("",var[1],var[3]))       
    


