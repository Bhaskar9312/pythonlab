class Converter:
    def __init__(self,length,unit):
        self.length=length
        self.unit=unit
        if(self.unit!='inches'):
            match(self.unit):
                case 'feet':
                    self.length=self.length*12
                    self.unit='inches'
                case 'yards':
                    self.length=self.length*36
                    self.unit='inches'
                case 'miles':
                    self.length=self.length*63360
                    self.unit='inches'
                case 'meters':
                    self.length=self.length*39.3701
                    self.unit='inches'
    def feet(self):
            return self.length/12
    def yards(self):
             return self.length/36
    def miles(self):
           return self.length/63360
    def meters(self):
           return self.length//39.3701
c=Converter(10,'miles')
print(c.feet())
print(c.yards())
print(c.meters())


