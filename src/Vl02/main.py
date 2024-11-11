from src.Vl02 import dog
from src.Vl02 import person

if __name__ == "__main__":
    mike = person.Student("mike", 20, "English")
    mike.get_age()
    mike.get_uni()

    goodboy = dog.PoliceDog("Rex", 120, "German Sheperd", "German")
    goodboy.bark()
    goodboy.rescue(mike)
    print(goodboy.rescued)
