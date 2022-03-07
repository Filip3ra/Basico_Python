"""
> Usar dois underlines antes do nome torna a variável privada
> Para acessar e alterar os valores privados eu preciso de funções na classe.
    Self: permite um objeto se referir a ele mesmo na classe.
    É uma forma de referir-se a um objeto da classe Animal.
> Construtores funcionam como em qualquer outra linguagem, definimos os valores e
usamos self para fazer a referência ao objeto em questão.
> Evitar usar a definição de privado com "__nome", pois não existem atributos privados em python.
Link dessa explicação aqui: https://pt.stackoverflow.com/questions/388253/como-sobrescrever-um-metodo
"""


class Animal:
    _name = None  # ou posso usar ""
    _height = 0
    _weight = 0
    _sound = 0

    # construtor
    def __init__(self, name, height, weight, sound):
        self._name = name
        self._height = height
        self._weight = weight
        self._sound = sound

    # getters e setters
    def set_name(self, name):
        self._name = name

    def set_height(self, height):
        self._height = height

    def set_weight(self, weight):
        self._weight = weight

    def set_sound(self, sound):
        self._sound = sound

    def get_name(self):
        return self._name

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def get_sound(self):
        return self._sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(
            self._name, self._height, self._weight, self._sound)


cat = Animal('Ninzera', 33, 10, 'Meow')

print(cat.toString())


class Dog(Animal):
    _owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self._owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self._owner = owner

    def get_owner(self):
        return self._owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} and his owner is {}".format(
            self._name, self._height, self._weight, self._sound, self._owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog("Spot", 53, 27, "Ruff", "Filipi")

print(spot.toString())

print(spot.multiple_sounds(5))  # por que está printando none?


# polimorfismo
class AnimalTesting:

    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()

# ao chamar o mesmo método 'get_type()' para animais diferentes temos respostas diferentes
test_animals.get_type(cat)
test_animals.get_type(spot)
