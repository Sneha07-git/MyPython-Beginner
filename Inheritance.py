# Parent Class
class User:
    def sign_in(self):
        print('logged in')


# Child class 1
class Wizard(User):  # Inherited User
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power with {self.power}')


#Child Class 2
class Archer(User):
    def __init__(self,name,num_arrows,arrows_left):
        self.name = name
        self.num_arrows = num_arrows
        self.arrows_left = arrows_left

    def check_attack(self):
        print(f'attacking with arrows =  {self.arrows_left}- {self.num_arrows}')

#Multiple Inheritance
class Hybrid(Wizard,Archer):
    def __init__(self, name,arrows_left,power,num_arrows):
        Archer.__init__(self,name,num_arrows,arrows_left)
        Wizard.__init__(self,name,power)

hyb = Hybrid('Hybrid',20,50,100)
print(hyb.attack())
print(hyb.check_attack())
print(hyb.sign_in())


'''
wiz1 = Wizard('abc',20)
arch1 = Archer('pqr',50,40)

wiz1.sign_in()
arch1.sign_in()
wiz1.attack()
arch1.attack()
'''