
class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type in self.__class__.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            self.__class__.all.append(self)
        else:
            raise Exception("Invalid pet_type")


class Owner:
    def __init__(self,name):
        self.name=name
    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner,Owner) and pet.owner==self]
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise Exception("pet must be an instance of Pet")
        else:
            pet.owner=self
    def get_sorted_pets(self):
        return sorted(self.pets(),key=lambda pet: pet.name)