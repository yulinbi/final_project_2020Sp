"""
Simulate the game of stroking the appropriate part of the kitten,
using basic Monte Carlo simulation techniques to get statistical results and analyze.
Game description:
There are four poses for kittens, "sleep,sit,stand,all fours"
and the corresponding scoring parts for each pose are different.
For example, in "sit", the scoring parts are 'back', 'foot1', 'foot3', 'head'
And heart representing user has touched scoring parts,
while thunder representing user hasn't touched correct part
The kitten switches its actions after being touched twice.
The user gains more than 5 hearts to win the game.
If a non-scoring part is encountered during the game, user will gain thunder,
and when the number of thunder is more than 3,  the user fails.

"""


import random



class General_User:
    #this type of user plays the game casually

    def __init__(self,name):
        self.name=name


    def touching_choice(self,p):
        """
        users randomly choose touching part
        :param p: pose
        :return choose:  list of touching part

        """
        choose = random.sample(part,2)

        return choose

    def learn(self,p,touch):
        pass

class Preferred_User(General_User):
    #this type of user has their own preference, for example, some people like to touch head while others prefer to touch stomach


    def __init__(self,name,tendency):
        super().__init__(name)
        self.tendency = None
        #self.possibility = None
        self.set_tendency(tendency)

    def set_tendency(self,t):
        """
        user's preference of choosing each part
        :param t: tuple of tendency of each part

        """

        if t is None:
            self.tendency=(1,1,1,1,1,1,1,1)
        else:
            self.tendency = t
        #a,b,c,d,e,f,g,h = self.tendency
        #self.possibility = sum(self.tendency)

    def touching_choice(self,p):
        """
        users have their preference to choose touching part
        :param p: pose
        :return choose: list of user's choice of touching parts

        """
        choose = []
        while len(choose) < 2:
            #for i in range(2):
            poss = random.randint(0,sum(self.tendency))

            if poss<= self.tendency[0]:
                if 'head' not in choose:
                    choose.append('head')
                continue
            elif poss<= self.tendency[0]+self.tendency[1]:
                if 'foot1' not in choose:
                    choose.append('foot1')
                continue
            elif poss<= self.tendency[0]+self.tendency[1]+self.tendency[2]:
                if 'foot2' not in choose:
                    choose.append('foot2')
                continue
            elif poss<= self.tendency[0]+self.tendency[1]+self.tendency[2]+self.tendency[3]:
                if 'foot3' not in choose:
                    choose.append('foot3')
                continue
            elif poss<= self.tendency[0]+self.tendency[1]+self.tendency[2]+self.tendency[3]+self.tendency[4]:
                if 'foot4' not in choose:
                    choose.append('foot4')
                continue
            elif poss<= self.tendency[0]+self.tendency[1]+self.tendency[2]+self.tendency[3]+self.tendency[4]+self.tendency[5]:
                if 'back' not in choose:
                    choose.append('back')
                continue
            elif poss<= self.tendency[0]+self.tendency[1]+self.tendency[2]+self.tendency[3]+self.tendency[4]+self.tendency[5]+self.tendency[6]:
                if 'stomach' not in choose:
                    choose.append('stomach')
                continue
            else:
                if 'tail' not in choose:
                    choose.append('tail')
                continue

        return choose


    def learn(self,p,touch):
        pass



class Smart_User(General_User):
    #this type of user is smart, they observe the previous result to determine which part they will touch in order to gain heart

    def __init__(self,name,p):
        self.select = {}
        for i in p:
            self.select[i] = []
        Smart_User.name=name


    def touching_choice(self,p):
        """
        users can choose touching part based on previous result
        :param p: pose
        :return users' choice
        """

        part = ['head', 'foot1', 'foot2', 'foot3', 'foot4', 'back', 'stomach', 'tail']
        if len(self.select[p]) == 0:
            return random.sample(part,2)
        elif len(self.select[p]) == 1:
            part.remove(self.select[p][0])
            c = random.sample(part,1)
            return [self.select[p][0], c[0]]
        else:
            return random.sample(self.select[p],2)



    def learn(self,p,touch):
        """"
        :param p:pose
        :param touch: dictionary, 0 represents thunder and 1 represents heart, for example: touch = {tail:0,foot1:1}
        :return select: dictionary of known scoring positions for each pose
        """

        for key, value in touch.items():
            if key in self.select[p]:
                pass
            elif value ==1:
                self.select[p].append(key)
        return self.select



posture = ['sleep', 'sit', 'stand', 'all fours']
part = ['head', 'foot1', 'foot2', 'foot3', 'foot4', 'back', 'stomach', 'tail']


def heart_tendency(p):
    """
    deterimine the weight of each part to represent heart in every pose
    :param p: pose of kitten
    :return: tendency: the preference part to get heart in each pose

    >>> heart_tendency('sit')
    (10, 2, 0, 4, 50, 60, 70, 80)
    >>> heart_tendency('stand')
    (0, 30, 1, 10, 40, 70, 10, 90)
    >>> heart_tendency('sleep')
    (1, 10, 120, 3, 40, 50, 8, 80)
    >>> heart_tendency('all fours')
    (50, 2, 20, 20, 20, 70, 80, 9)


    """

    if p == 'sit':
        tendency = (10,2,0,4,50,60,70,80)
    if p == 'stand':
        tendency = (0,30,1,10,40,70,10,90)
    if p == 'sleep':
        tendency = (1,10,120,3,40,50,8,80)
    if p == 'all fours':
        tendency = (50,2,20,20,20,70,80,9)

    return tendency


def heart(tendency):
    """
    :param tendency: the preference part to get heart in each pose
    :return heart: list of scoring heart parts in each pose

    >>> heart(heart_tendency('sit'))
    ['foot4','back','stomach','tail']
    >>> heart(heart_tendency('stand'))
    ['foot1','foot4','back','tail']
    >>> heart(heart_tendency('sleep'))
    ['foot2',''foot4','back','tail']
    >>> heart(heart_tendency('all fours'))
    ['head','foot3','back','stomach']




    """
    heart= []
    #poss = random.randint(0,sum(tendency))
    while len(heart) <4:
        poss = random.randint(0, sum(tendency))
        if poss <= tendency[0]:
            if 'head' not in heart:
                heart.append('head')
            continue
        elif poss <= tendency[0] + tendency[1]:
            if 'foot1' not in heart:
                heart.append('foot1')
            continue
        elif poss <= tendency[0] + tendency[1] + tendency[2]:
            if 'foot2' not in heart:
                heart.append('foot2')
            continue
        elif poss <= tendency[0] + tendency[1] + tendency[2] + tendency[3]:
            if 'foot3' not in heart:
                heart.append('foot3')
            continue
        elif poss <= tendency[0] + tendency[1] + tendency[2] + tendency[3] + tendency[4]:
            if 'foot4' not in heart:
                heart.append('foot4')
            continue
        elif poss <= tendency[0] + tendency[1] + tendency[2] + tendency[3] + tendency[4] + tendency[5]:
            if 'back' not in heart:
                heart.append('back')
            continue
        elif poss <= tendency[0] + tendency[1] + tendency[2] + tendency[3] + tendency[4] + tendency[5] + tendency[6]:
            if 'stomach' not in heart:
                heart.append('stomach')
            continue
        else:
            if 'tail' not in heart:
                heart.append('tail')
            continue


    return heart
def game(user):
    """"
    the whole process fo the game
    :param user: type of user
    :return 1 represents success or 0 represents failure

    >>> zzj=General_User('zzj')
    >>> game(zzj)
    1
    >>> zenith = Preferred_User('zenith',(10,200,3,50,70,90,4,100))
    >>> game(zzj)
    0
    >>> jjj = Smart_User('jjj',posture)
    >>> game(jjj)
    1

    """

    #touch = {}
    heart_num = 0
    thunder_num = 0
    touching_num = 0

    while heart_num < 5 and thunder_num < 3:
        touch = {}

        #if touching_num % 2 == 0:
        p = random.choice(posture)
        #print('Posture is ' + g)
        h = heart(heart_tendency(p))

        touching = user.touching_choice(p)
        #print(touching)
        for i in range(len(touching)):
            if touching[i] in h:
                heart_num += 1
                touch[touching[i]] = 1

            else:
                thunder_num += 1
                touch[touching[i]] = 0
        user.learn(p,touch)
        #touching += 1
        #touching_num += 1

    if heart_num >= 5:
        return 1
    if thunder_num >= 3:
        return 0




if __name__ == '__main__':
    posture = ['sleep', 'sit', 'stand', 'all fours']
    a=0
    b=0
    c=0
    #define different type of user
    #general user
    yulinbi = General_User('yulin')
    #user with preference
    lyn = Preferred_User('lyn',(100,2,30,4,50,6,7,80))
    #attentive user
    linda = Smart_User('linda',posture)
    for i in range(1000000):
        a += game(yulinbi)
        b += game(lyn)
        c += game(linda)

    print('\n-----------------------------------------------------------------')
    print('yulinbi')
    print('successful rate is {:.4f}'.format(a/1000000))
    print('\n-----------------------------------------------------------------')
    print('lyn')
    print('successful rate is {:.4f}'.format(b/1000000))
    print('\n-----------------------------------------------------------------')
    print('linda')
    print('successful rate is {:.4f}'.format(c/1000000))
    print('\n-----------------------------------------------------------------')








































