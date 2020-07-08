class CaseData(object):
    def __init__(self,*args,**kwargs):
        obj = list(*args)
        for i in obj:
            setattr(self,i[0],i[1])
