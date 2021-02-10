class Cell():
    def __init__(self, position, status):
        self.position = position
        self.status = status

    def getLiberties(self):
        x = int(self.position[0])


x = input("wie groß soll das Feld sein?")
x = int(x)
for i in range(x):
    print(i)
    for j in range(x):
        print(j)
        #field = {Cell( str(i+"/"+j), "empty")}

#print (field)