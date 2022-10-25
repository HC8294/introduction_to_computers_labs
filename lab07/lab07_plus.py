class Animal():#建立類別Animal

  def __init__(self, weight, mood):  #對類別進行初始化
    self.weight = weight
    self.mood = mood
  def feed(self):
    pass
  def walk(self):
    pass
  def bath(self, n_bath):
    pass

class Dogs(Animal):#建立子類別Dogs
  def __init__(self, weight, mood):
    super().__init__(weight, mood)
  def feed(self, n_feed):#每次吃飯時體重增加0.2心情加1
    self.weight = self.weight + 0.2 * n_feed
    self.mood = self.mood + 1 * n_feed
  def walk(self, n_walk):#每次散步時體重減0.2心情加2
    self.weight = self.weight - 0.2 * n_walk
    self.mood = self.mood + 2 * n_walk
  def bath(self, n_bath):#每次洗澡時心情減2
    self.mood -= n_bath * 2
  def printf(self, n_feed, n_walk, n_bath):
    print("狗狗現在的體重=" + str(self.weight) + "kg,心情=" + str(self.mood))#輸出狗勾體重和心情


class Shiba(Dogs):

  def __init__(self, weight, mood):
    super().__init__(weight, mood)

  def feed(self, n_feed):  #覆寫原Dog裡的feed方法
    self.weight += n_feed * 0.3  #每feed一次,體重+0.3
    self.mood += n_feed * 5  #每feed一次,心情+5

  def printf(self, n_feed, n_walk, n_bath):  #建立新方法
    self.feed(n_feed)
    self.walk(n_walk)
    self.bath(n_bath)
    print("柴犬現在的體重=", self.weight, "kg,心情", self.mood)

  def mood_constraint(self, constraint):
    self.constraint = constraint
    if self.mood >= constraint:
      self.mood = constraint
      print("所以，柴犬現在的心情", self.mood)
    print("mood最高只能為=", self.constraint)


shiba = Shiba(5, 70)
shiba.printf(20, 10, 3)
shiba.mood_constraint(90) 
shiba = Shiba(5, 70)
shiba.printf(20, 10, 3)
shiba.mood_constraint(300) #設定心情最大值