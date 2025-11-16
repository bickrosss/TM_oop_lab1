class Pet:
    kind = "mammal"
    n_pets = 0
    pet_names = []

    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4
print("создание экземпляров:")
tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Benjamin")

print(f"Число питомцев: {Pet.n_pets}")
print(f"Имена питомцев: {Pet.pet_names}")
print()

# доступ к атрибуту через класс
print("изменение атрибутов класса:")
Pet.n_pets = 3
print(Pet.n_pets)
print(tom.n_pets)
print(avocado.n_pets)
print(ben.n_pets)

# изменение через экземпляры
print("изменение через экземпляры:")
tom.n_pets += 1
avocado.n_pets += 1
ben.n_pets += 1

print(Pet.n_pets)
print(tom.n_pets)
print(avocado.n_pets)
print(ben.n_pets)

ben.kind = "fish"

print(Pet.kind)
print(tom.kind)
print(avocado.kind)
print(ben.kind)

# добавление имен в общий список
print("добавление имен:")
tom.pet_names.append(tom.name)
avocado.pet_names.append(avocado.name)
ben.pet_names.append(ben.name)

print(Pet.pet_names)
print(tom.pet_names)
print(avocado.pet_names)
print(ben.pet_names)

# создание отдельных списков для каждого экземпляра
print("создание отдельных списко:")
tom.pet_names = ["Tom"]
avocado.pet_names = ["Avocado"]
ben.pet_names = ["Benjamin"]

print(Pet.pet_names)
print(tom.pet_names)
print(avocado.pet_names)
print(ben.pet_names)

# изменение атрибутов
print("изменение атрибутов")
ben.legs = 0
print(ben.legs)
print(tom.legs)
print(avocado.legs)

# добавление атрибутов
print("добавление новых атрибутов к классу:")
Pet.all_specs = [tom.spec, avocado.spec, ben.spec]

print(Pet.all_specs)
print(tom.all_specs)
print(avocado.all_specs)
print(ben.all_specs)

avocado.breed = "corgi"
print(avocado.breed)
