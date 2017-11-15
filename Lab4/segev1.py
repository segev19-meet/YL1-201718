class Animal(object):
    def __init__(self,sound,name,age,favorit_color):
        self.sound=sound
        self.name=name
        self.age=age
        self.favorit_color = favorit_color
    def eat(self,food):
        print(" yummyyyyyyy!!"+ self.name +" is eating"+food)
    def description(self):
        print (self.name+ " is "+ str(self.age) +" years old and loves the color "+ self.favorit_color)
    def make_sound(self):
        print(self.sound*3)
    def talk(self,sentence):
        print(sentence)
    def kiss(self,sentence):
        print(sentence)
class Person(object):
    def __init__(self, name, age, city, gender):
        self.name=name
        self.age=age
        self.city=city
        self.gender=gender
    def eat(self,food):
        print("ellen is eating"+food)


class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
        print(lyrics)
        


j=Animal("oooouuuuaaarrrhhhhhhhh","Lion",23,"green")
j.eat("fish")
j.description()
j.make_sound()
j.talk("hi")
j.kiss("bbbbbblluuuaaajjhhaaaaa")
allen = Person("allen",32,"Tel-Aviv","male")
allen.eat("fish")
hi = Song("Roses are red,Violents are blou,I wrote this poem for you!!!!!")


