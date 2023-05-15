# Exercise 3 : Dogs Domesticated ----------------------------------------------------
from exercicesXP import Dogs

class PetDog(Dogs):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
        print(self.bark())
        self.trained = True
    
    def play(self, *name):
        print(f"{name} all play together")
    
    def do_a_trick(self, name):
        import random
        sentences = [f"{self.name} does a barrel roll", f"{self.name} stands on his back legs ", f"{self.name} shakes your hand", f"{self.name} plays dead"]
        random_sentence = random.choice(sentences)
        print(random_sentence)



dog1 = PetDog("Bob", 8, 20)
dog2 = PetDog("Lili", 5, 30)
dog3 = PetDog("Bubu", 3, 8)

dog1.play(dog2.name, dog3.name, dog1.name)

dog1.do_a_trick(dog1)