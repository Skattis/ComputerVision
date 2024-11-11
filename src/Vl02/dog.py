class Dog:
    def __init__(self, name, size, breed):
        self.name = name
        self.size = size
        self.breed = breed

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_breed(self):
        return self.breed

    def bark(self):
        print("bark")


class PoliceDog(Dog):
    def __init__(self, name, size, breed, nationality):
        super().__init__(name, size, breed)
        self.nationality = nationality
        self.rescued = []

    def rescue(self, person):
        self.rescued.append(person.get_name())
        print(f"Give me a treat already! I rescued {person.get_name()}")
