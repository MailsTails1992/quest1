import time
inventory = []
q = 0
w = 0
e = 0
r = 0
t = 0
y = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
z = 0
p = 0
eastereggs = 0
EE1 = False
EE2 = False
EE3 = False
EE4 = False
EE5 = False
EE6 = False
leads = 0
lead1 = False
lead2 = False
lead3 = False
lead4 = False
lead5 = False
path = False
key1 = False
input("You: Where am i? How did I end up here? Who am I? I don't remember anything...")
input('Unknown1: You came to my game to survive to pass all the tests!')
input('What the hell is going on here?')
input('You look around the room and see that there is a bed, a closet, a drawer, a door. What will you do?')
print('Get under the bed look in the closet climb the drawer open the door')
while a!= 'Get under the bed' or 'look in the closet' or 'climb the drawer'  or'open the door':
    a = input()
    if a  =='Get under the bed':
        if EE1 == False:
            input('You got under the bed')
            input('Theres nothing here')
            input('ITS AN EASTER EGG FROM GRANNY DUDE')
            eastereggs = eastereggs + 1
            EE1 = True
        elif EE1 == True:
            input('Youve been here before, dude...')
            input('Farm Easter eggs is dirty..')
    elif a  =='look in the closet':
        input('You decided to look in the closet')
        input('It was buzzing strangely')
        input('You opened it')
        input('There were chainsaws')
        input('You:Is that a chainsaw cabinet?')
        input('Then you were pushed into it and you turned into mincemeat')
        input('Unknow2:FOOD IS SERVED')
        exit()


    elif a  =='climb the drawer':
        if key1 == False and lead1 == False:
            input('You looked in the drawer')
            input('You found the note and the key')
            inventory.append('key1')
            key1 = True
            lead1 = True
        else:
            input('Theres nothing here')
        input('The note said: Be careful, this sick psychopath put traps and monsters here. I..')
        input('The note ended')
        input('Apparently the author died from those very monsters...')
        leads = leads + 1
    elif a == 'open the door':
        input('You decided to try to open the door')
        if 'key1' not in inventory :
            input("You can't open the door!")
            input('Find a key')
        elif 'key1' in inventory:
            input('You opened the door!')
            inventory.remove('key1')
            break
input("Well, well, well, You can't open the door!")
input("What awaits me next?")
input("You look around and ask: What to do?")
input("Unknown1: This is a maze you have to get out of it.")
input(" And how lucky you are there are surprises here!")
input('You: God damn')
input('Where will you go?')
input('Forward Left Right Back')
while b!= 'Left' or 'Right' or 'Back' or 'Forward':
    b = input()
    if b == 'Left':
        input('You looked left, but your passed out...')
        exit()
    elif b == 'Back':
        input('strange but the door is locked, you turned around and passed out...')
        exit()
    elif b == 'Right':
        input('You turned right. There is a long corridor. Walk through it?')
        input('yes  no')
        while c!= 'yes' or 'no': 
            c = input()
            if c == 'no':
                break
            else:
                if path == True:
                    input('Its still the same table, but you shouldnt have come back here')
                    input('You died')
                    exit()
                    break
                else:
                    path = True
                    input('You went down the corridor there was a note f l f l f r')
                    input('what is it?')
                    break
    elif b == 'Forward':
        if path == False:
            input('look for something, door is open')
        if path == True:
            input('you saw some screen .. there you need to enter a six-digit code but there are only buttons: forward back to the left right')
            while q!= 'forward' or 'left' or 'right' or 'down' and w!= 'forward' or 'left' or 'right' or 'down' and e!= 'forward' or 'left' or 'right' or 'down' and r!= 'forward' or 'left' or 'right' or 'down' and t!= 'forward' or 'left' or 'right' or 'down' and y!= 'forward' or 'left' or 'right' or 'down' and q!= 'forward' or 'left' or 'right' or 'down':
                q = input('forward left right down')
                if q == 'forward' and w == 'left' and e == 'forward' and r == 'left' and t == 'forward' and y == 'right':
                    input('You entered the correct code! you entered what looked like an elevator and took the route that was in the code...wait the note')
                    z = time.time()
                    input('press enter to collect the note')
                    m = time.time()
                    if m - z > 1:
                        pass
                    elif m - z <= 1:
                        leads = leads + 1
                    input('un1: you pass that level')
                    input('i like puzzels especially for a time')
                    input('are you pass this level?')
                    input('puzzel one')
                    input('The cauldron boils in the forest without fire.')
                    l = input()
                    z = time.time()
                    time.sleep(5)
                    m = time.time()
                    if m - z > 5:
                        input('you are dead')
                        exit()
                    elif m - z <= 5:
                        if l!= 'anthill' or 'муравейник':
                            input('you are dead')
                        else:
                            input('you correct')
                    input('There are a hundred holes with a hole in a hole, a hole.')
                    z = time.time()
                    time.sleep(5)
                    m = time.time()
                    if m - z > 5:
                        input('you are dead')
                        exit()
                    elif m - z <= 5:
                        if l!= 'thimble' or 'наперсток':
                            input('you are dead')
                        else:
                            input('you correct')
                    input('They lead us forward, although they always walk in a circle')
                    z = time.time()
                    time.sleep(7)
                    m = time.time()
                    if m - z > 7:
                        input('you are dead')
                        exit()
                    elif m - z <= 7:
                        if l!= 'hands on the clock' or 'стрелки на часах':
                            input('you are dead')
                        else:
                            input('you correct') 
                    input('It can talk, but it wont show anything for sure.')
                    z = time.time()
                    time.sleep(4)
                    m = time.time()
                    if m - z > 4:
                        input('you are dead')
                        exit()
                    elif m - z <= 4:
                        if l!= 'radio' or 'радио':
                            input('you are dead')
                        else:
                            input('you correct')
                    input('What is divided in half only once every four years?')
                    z = time.time()
                    time.sleep(6)
                    m = time.time()
                    if m - z > 6:
                        input('you are dead')
                        exit()
                    elif m - z <= 6:
                        if l!= 'Year by day' or 'год по дням':
                            input('you are dead')
                        else:
                            input('you correct')
                            input('then you saw some kind of door and knocked it down. There were some people and some professor there, not understanding how, but you realized that the professor was the one who conducted the tests on you')
                            input('you will want kill him')
                            print('what you be going to do?')
                            input('kill    call the police   sell it for organs')
                            while p!= 'kill' or 'call the police' or 'sell it for organs':
                                if p == 'kill':
                                    input('you attacked him with a splinter that you found and killed him, but the police came and detained you because you killed a human')
                                    print('you guitly')
                                    print('bad ending')
                                    exit()
                                elif p == 'call the police':
                                    input('You called the police and they came. Then the surveys began.')
                                    if leads < 2:
                                        input('The police didnt find enough evidence, so you were detained on false charges.')
                                        print('you guitly')
                                        print('dumb ending')
                                        exit()
                                    else:
                                        input('The police found you innocent and arrested him')
                                        print('good ending')
                                        exit()
                                elif p == 'sell it for organs':
                                    input('You decided to sell him for organs. You became very rich but then the police came to you. She saw what you were doing.')
                                    if leads < 2:
                                        input('The police arrested you for the black market. You were executed.')
                                        print('you dead')
                                        print('worst ending')
                                        exit()
                                    else:
                                        input('You showed a fake permit for this and the police believed you.')
                                        print('THE BEST ending')
                                        exit()
                                    
                            

                else:
                    input('You dialed the wrong code, but the door was opened for you. There was a room there. When you entered you were crushed.')
                    exit()
