#!/usr/bin/python3

class animalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class duck(animalActions):
    strings = dict(
        quack = "Quaaaaaaaak!",
        feathers = "The duck has grey and white feathers.",
        bark = "The duck cannot Bark.",
        fur = "The duck has no fur."
    )

class person(animalActions):
    strings = dict(
        quack = "The Person Imitates the duck",
        feathers = "The person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat"
    )

class dog(animalActions):
    strings = dict(
        quack = "The dog cannot quack",
        feathers = "the dog has no feathers",
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )

def inTheDogHouse(dog):
    print(dog.bark())
    print(dog.fur())

def inTheForest(duck):
    print(duck.quack())
    print(duck.feathers())


def main():
    Donald = duck()
    John = person()
    Fido = dog()


    print("_ In the forest")
    for o in (Donald,John,Fido):
        inTheForest(o)

    print("_ In the forest")
    for o in (Donald,John,Fido):
        inTheDogHouse(o)

if __name__ == "__main__": main()



