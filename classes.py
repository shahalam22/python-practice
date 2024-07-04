# # a basic class

# class TestClass:
#     test_var = (1,2,3)
#     another_var = 'something'

#     def test_func(self):        # self is a reference to the instance of the class (like this in Java)
#         print('Function in a class')
#         self.another_func('test from inside')

#     def another_func(self, test_param):
#         print(test_param)

# # create instance of class
# test = TestClass()
# print(test.test_var)
# print(test.another_var)

# test.another_var = 'new value'
# print(test.another_var)

# test.test_func()
# test.another_func('test')


# # maze class

# class Maze:
#     def __init__(self, health, mana):       # works like a constructor
#         self.health = health
#         self.mana = mana
#         print('the maze class was created')
#         print(self.health)

#     # def __len__(self):            # works like a getter  
#     #     return self.health
    
#     def attack(self, target):
#         target.health -= 10

# class Monster:
#     health = 100

# maze = Maze(100, 200)
# monster = Monster()

# # print(len(maze))

# print(monster.health)
# maze.attack(monster)
# print(monster.health)


# # inheritance
# class Human:
#     def __init__(self, health):
#         self.health = health

#     def attack(self):
#         print('attacks')

# class Warrior(Human):
#     def __init__(self, health, defense):
#         super().__init__(health)
#         self.defense = defense

# class Barbarian(Human):
#     def __init__(self, health, damage):
#         super().__init__(health)
#         self.damage = damage

# warrior = Warrior(100, 5.5)
# barbarian = Barbarian(200, 8.1)
# warrior.attack()
# barbarian.attack()


# # exercise

# class Entity:
#     def attack(self):
#         print(f'attack with {self.damage} damage')

# class Monster(Entity):
#     def __init__(self, health, damage):
#         self.health = health
#         self.damage = damage

#     def __repr__(self):     # works like a getter method. Must need to print monster instance
#         return f'Monster with {self.health} health and {self.damage} damage'

# monster = Monster(100, 10)
# monster.attack()

# print(monster)