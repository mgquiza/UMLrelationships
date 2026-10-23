class Dining_area:
    def __init__(self, name):
        self.name = name
        self.chairs = []

    def add_chair(self, chair):
        self.chairs.append(chair)

    def list_chairs(self):
        return [f"{chair.model} by {chair.producer}" for chair in self.chairs]

    

class Chair:
    def __init__(self, producer, model):
        self.producer = producer
        self.model = model


dining_area = Dining_area("MickeyMouse_Foodhouse")

chair1 = Chair("Elloise James","Archengine")
chair2 = Chair("Ellow James", "DullKnife")
chair3 = Chair("???", "N/a") 

dining_area.add_chair(chair1)
dining_area.add_chair(chair2)
dining_area.add_chair(chair3)

print (dining_area.name)

for chair in dining_area.list_chairs():
    print(chair)