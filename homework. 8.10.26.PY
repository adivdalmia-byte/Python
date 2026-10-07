class Dog:
    species="mammal"
    def __init__(self,colour,breed):
        self.colour=colour
        self.breed=breed
y= Dog("gold", "golden retriever")
x=Dog("black","shitzu")

print("gold is the colour {}".format(y.breed))
print("black is also the colour {}".format( x.breed))

