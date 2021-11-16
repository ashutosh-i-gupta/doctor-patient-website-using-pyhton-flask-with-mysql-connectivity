class Patient:
    def __init__(self,pid,pfname,plname,pgender,pnumber,paddress,pstate,pcity,pzipcode,pemail,password,pdisease,dfname):
        self.pid=pid
        self.pfname=pfname
        self.plname=plname
        self.pgender=pgender
        self.pnumber=pnumber
        self.paddress=paddress
        self.pstate=pstate
        self.pcity=pcity
        self.pzipcode=pzipcode
        self.pemail=pemail
        self.password=password
        self.pdisease=pdisease
        self.dfname=dfname
    def __str__(self):
        return f'Patient[{self.pid},{self.pfname},{self.plname},{self.pgender},{self.pnumber},{self.paddress},{self.pstate},{self.pcity},{self.pzipcode},{self.pemail},{self.password},{self.pdisease},{self.dfname}]'
