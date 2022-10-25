class Animal(): #建立類別Animal
    def __init__(self, weight, mood):#對類別進行初始化
        self.weight = weight
        self.mood = mood
    def feed(self):
        pass
    def walk():
        pass
    def bath():
        pass#跳過函式
    
class Dogs(Animal):#建立子類別Dogs
    def __init__(self, weight, mood):
        super().__init__(weight,mood)
    def feed(self,n_feed):#每次吃飯時體重增加0.2心情加1
        self.weight =self.weight+0.2*n_feed
        self.mood =self.mood+1*n_feed
    def walk(self,n_walk):#每次散步時體重減0.2心情加2
        self.weight =self.weight-0.2*n_walk
        self.mood =self.mood+2*n_walk
    def bath(self,n_bath):#每次洗澡時心情減2
        self.weight =self.weight+0*n_bath
        self.mood =self.mood-2*n_bath
    def printf(self, n_feed, n_walk, n_bath):#輸出狗勾體重和心情
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("狗狗現在的體重=" + str(self.weight) + "kg,心情=" + str(self.mood))


class Cats(Animal):#建立子類別Cats
    def __init__(self, weight, mood):
        super().__init__(weight,mood)
    def feed(self,n_feed):#每次吃飯時體重增加0.1心情加1
        self.weight =self.weight+0.1*n_feed
        self.mood =self.mood+1*n_feed
    def walk(self,n_walk):#每次散步時體重減0.1心情減1
        self.weight =self.weight-0.1*n_walk
        self.mood =self.mood-1*n_walk
    def bath(self,n_bath):#每次洗澡時心情減2
        self.weight =self.weight+0*n_bath
        self.mood =self.mood-2*n_bath
    def printf(self, n_feed, n_walk, n_bath):#輸出卯貓體重和心情
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("貓貓現在的體重=" + str(self.weight) + "kg,心情=" + str(self.mood))


dog = Dogs(4.8, 65) #定狗勾原本體重和心情
dog.printf(18, 10, 4) #對狗勾使出printf函式!

cat = Cats(8.2, 60) #定卯貓原本體重和心情
cat.printf(40, 7, 1)#對卯貓使出printf函式!