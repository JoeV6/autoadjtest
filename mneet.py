import random
import time

class adjust:

    spot_range = []
    currentadj = None
    cannon_mode = None
    adjust_mode = None
    raidtimer = 1
    first = None
    t = None



    def setSpotRange(self, s_min, s_max):
        self.spot_range = [s_min, s_max]

    def setMode(self, a_mode):
        self.adjust_mode = a_mode

    def setReg(self):
        self.cannon_mode = 0

    def setAlly(self):
        self.cannon_mode = 1




    def getRandomAdj(self, shot):

        current = random.randint(int(shot) - 20, int(shot))

        if current < self.spot_range[0]:
            current = int(self.spot_range[1])

        return current


    def getStairAdj(self, shot):
        
        current = int(shot) - 2

        if current < self.spot_range[0]:
            current = int(self.spot_range[1])

        return current

    def getUpDownAdj(self):

        i = random.randint(1,2)

        if i == 1:
            c = self.spot_range[1] - random.randint(0,6)
        else:
            c = self.spot_range[0] + random.randint(0,6)

        return c

    def getTopAdj(self):
        
        c = self.spot_range[1]

        return c

    def getLowAdj(self):

        c = self.spot_range[0] + random.randint(0,6)

        return c

    def getHighAdj(self):

        c = self.spot_range[1] - random.randint(0,6)

        return c



adj = adjust()
adj.setSpotRange(200, 255)
adj.setReg()
adj.currentadj = 255
adj.first = True
adj.t = 0.5

def shoot(f):
    adj.currentadj = f
    print("shooting " + str(f))
    adj.raidtimer = adj.raidtimer + 1
    time.sleep(adj.t)





while True:

    print("------Next-Phase------")
    print("time : " + str(adj.raidtimer))
    
    if adj.first:
        shoot(255)
        adj.first = False
        continue
    
    if adj.raidtimer < 20: r = 7
    elif adj.raidtimer < 50: r = random.choice([2,5,7])
    else: r = random.randint(1,7)

    if r == 1:
        print("RandomAdjusting")
        for i in range(random.randint(3,8)):
            shoot(adj.getRandomAdj(adj.currentadj))
    elif r == 2:
        print("StairCasing")
        for i in range(random.randint(3,8)):
            shoot(adj.getStairAdj(adj.currentadj))
    elif r == 3:
        print("UpDowning")
        for i in range(random.randint(3,8)):
            shoot(adj.getUpDownAdj())
    elif r == 4:
        print("Low")
        for i in range(random.randint(3,8)):
            shoot(adj.getLowAdj())
    elif r == 5:
        print("high")
        for i in range(random.randint(3,8)):
            shoot(adj.getHighAdj())
    elif r == 7:
        print("Top")
        for i in range(random.randint(3,5)):
            shoot(adj.getTopAdj())



