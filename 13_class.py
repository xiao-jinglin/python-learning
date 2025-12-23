class Animal:
    def __init__(self, name, age, species, hp, power):
        self.name = name
        self.age = age
        self.species = species
        self.hp = hp
        self.power = power  

    def introduce(self):
        print(f"{self.name}は{self.age}歳の{self.species}です")

    def attack(self, target):
        print(f"{self.name}は{target.name}に攻撃した！")
        target.hp -= self.power
        print(f"{target.name}の残りHPは{target.hp}です")
        if not target.is_alive():
            print(f"{target.name}は倒れた！")

    def is_alive(self):
        return self.hp > 0
    
dog = Animal("ポチ", 3, "犬", 100, 10)
cat = Animal("タマ", 2, "猫", 80, 15)
dog.introduce()
cat.introduce()

while dog.is_alive() and cat.is_alive():
    dog.attack(cat)
    if cat.is_alive():
        cat.attack(dog)

