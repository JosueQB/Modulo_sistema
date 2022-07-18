class usuario():
    def __init__(self,Nombre,Cedula,Telefono,Correo):
        self.nombre=Nombre
        self.cedula=Cedula
        self.telefono=Telefono
        self.correo=Correo
        self.lista=[]
        self.nota=[]
        self.dic={}
        self.usu=[]
        
    def registra(self):
        while True:
            valor = str(input("{} ".format("Ingrese Nombres Completos:")))
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
    
        
        
            
    def MostrarEstudiante(self):
        print("{:15}{:25}{}".format(self.nombre,self.apellido,self.correo))
    def MostarDocente(self):
        print("{}{:5}{}".format(self.nombre,self.apellido,self.correo))
    def MostrarAdmin(self):
        print("{}{:5}{}".format(self.nombre,self.apellido,self.correo))       
    
    def ingreso(self,clave):
        Elementos=""
        while Elementos != clave:
            Elementos = (input("Clave de Ingreso: "))
            if Elementos==clave:
                print("ingreso")
                 
                     
    def CUsuarioD(self):
        ClaveD="Docente2022"
        return ClaveD
    def CUsuarioE(self):
        ClaveE="Estu2022"
        return ClaveE
    def CUsuarioA(self):
        ClaveA="Admin2022"
        return ClaveA
                
    
    def IngresoAdmin(self,UsuA="Admin"):
        Usu=""
        while Usu != UsuA:
            nom=(input("Ingrese su Usuario:"))
            if nom == UsuA:
                return nom
            
            
    def IngresoDocente(self,UsuD="dvera"):
        Usu=""
        while Usu != UsuD:
            nom=(input("Ingrese su Usuario:"))
            if nom == UsuD:
                return nom   
            
                       
    def IngresoEstudiante(self,UsuE="rquijije"):
        Usu=""
        while Usu != UsuE:
            nom=(input("Ingrese su Usuario:"))
            if nom == UsuE:
                return nom
        
             
    
un=usuario("Rolando Josue","0941483018","0961329155","jquijije@gmail.com")
# p=un.CUsuarioA()
# un.MostrarEstudiante()
# un.IngresoAdmin()
# un.ingreso(p)
n=un.registra()
print(n)
n2=un.registraCed()
print(n2)