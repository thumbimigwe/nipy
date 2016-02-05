#!/usr/bin/python3
# POLYMORPHISM EXAMPLE

# -- VIEW --
class animalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

    def _doAction(self, action):
        if action in self.strings:
            return self.strings
        else:
            return 'The {} nas No {}'.format(self.animalName(),action)

    def animalName(self):
        return self.__class__.name__.lower()


# -- MODEL --
class duck(animalActions):
    strings = dict(
        quack = "Quaaaaaaaak!",
        feathers = "The duck has grey and white feathers.",
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
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )


# -- CONTROLLER --

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