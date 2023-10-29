class Pet:

    all = []

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=False):
        self._name = name
        self._owner = owner
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception(f"Pet type must be in this list: {self.PET_TYPES}")
        type(self).all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        self._pet_type = pet_type
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        self._owner = owner

class Owner:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception(f"{pet} is not a valid pet")
    
    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key=lambda x: x.name)