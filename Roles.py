class Profesor: 
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
    
    
class Estudiante: 
    def __init__(self,id,nombre,cedula,materia,calificaiones,Asistencia):
        self.__id = id
        self.nombreE = nombre
        self.cedulaE = cedula
        self.materiaE=materia
        self.cal = calificaiones
        self.asis = Asistencia
       
    @property
    def id(self):
        return self.__id

    def getEstudiante(self):
        return  [str(self.id),self.nombreE,self.cedulaE,self.materiaE,self.cal,self.asis]

class Rol():
    def __init__(self):        
        self.lista=[]
        self.nota=[]
        self.mat=["Ingenieria de Software","Programacion Orientada a Objetos","Base de Datos"]
        self.longitud=0
        self.size=50
        self.dic={}
        
    #ADMINISTRADOR        
    def Adminañadir(self,nombre,cedula,materia,calificaiones,Asistencia):  
        if self.longitud < self.size:
            self.lista += [nombre,cedula,materia,calificaiones,Asistencia]
            self.longitud +=1
            return True
        else:
            return False 
       
    
    def Adminañadir2(self,dato):  
        if self.longitud < self.size:
            self.nota += [dato]
            self.longitud +=1
            return True
        else:
            return False 
        
        
    def Adminañadir3(self,dato):  
        if self.longitud < self.size:
            self.mat += [dato]
            self.longitud +=1
            return True
        else:
            return False
        
        
        
    def Adminmostrar(self):
        print("{}{:8}".format("","Estudiantes"))
        print("[{:8}] ".format(self.nombreE))
            
            
    def Admineliminar (self,dato):
        res=self.AdminBuscar(dato)
        if res != -1:
            for pos,ele in enumerate(self.lista):
                if ele== dato:
                    elim=self.lista[pos]
                    self.lista=self.lista[:pos] + self.lista[pos+1:]
                    self.longitud-=1       
                    return elim,self.lista
        else:
            return None
                
    def AdminBuscar(self,dato):  
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==dato:
                enc=True
                break
        if enc==True:
           return pos
        else:
            return -1 
        
    #ESTUDIANTE
    def EstuMostrar(self):
        print("{:3}{:9} {}".format("","Estudiantes","Posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:8}]  {:5}".format(ele,pos))
    

    def DocenteMostrar(self):
        print("{:5}{:19} {:19}{}".format("","Estudiantes","Calificacion", "Materia"))
                    
    def DocenteMat(self):
        print("{:5}{}".format("","Mis Materia"))
        print(self.mat[0])
    
    
    def DocenteAlumnnos(self):
        print("{:5}{}".format("","Mis Alumnos"))
        
        
    def AñadirDic(self):
        for ele in self.lista:
            self.dic[ele]=ele
        print(self.dic)
        
        
    def AñadirDic2(self):
        for ele in self.nota:
            self.dic[ele]=ele     
        print(self.dic)
        
