class Phone:
    def __init__(self):
        print ("Power On")

    def open(self):
        print ("Phone ready")
        

class youtube:
    def __init__(self, phone):
        self.phone = phone 

    def open_youtube(self):
        print ("launching app...")
        self.phone.open()
        print ("Youtube is playing")


my_phone = Phone()

my_Youtube = youtube(my_phone)

my_Youtube.open_youtube()