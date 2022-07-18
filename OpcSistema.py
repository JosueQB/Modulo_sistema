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
    
            
        
