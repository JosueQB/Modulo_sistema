
class Rol():
    def __init__(self):        
        self.lista=[]
        self.nota=[]
        self.mat=["Ingenieria de Software","Programacion Orientada a Objetos","Base de Datos"]
        self.longitud=0
        self.size=50
        self.dic={}
        
           
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
        
