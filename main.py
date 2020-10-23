import datetime as time
now = time.datetime.now()
hour = now.hour

if hour < 12:
    print("Good morning")
elif hour >= 12 and hour <= 18:
    print("Good afternoon")         
elif hour > 18 and hour < 19: 
    print("Good evening")
else:
    print('Have a nice night.')

def name():
    global nam
    nam = input('please input your name: ')
    if nam == '' or nam == ' ':
        print('you have inputed nothing try again')
        name()
    else:
        print('Thank you ',nam)
        print('''
        ''')
name()
def gender():
    global gend
    gend = input('''Are you:
    male(m) 
    female(f)
    diclose(d)
    pls provide the replay here:''')
    global female
    female = 'lady'
    if gend == 'male' or gend == 'm':
        print('Thank you Mr ',nam)
    elif gend == 'female'or gend == 'f':
        print('Thank you',female,nam)
    elif gend == 'diclose' or gend == 'd':
        print('Thank you ',nam,'! We respect your right to not tell us')
    elif gend == ' ' or gend == '':
        print('you have inputed nothing try again')
        gender()
    elif gend != 'male' or con != 'lady' or gend == 'm' or gend == 'f'or gend == '1'or gend == '2':
        print('you have inputed the wrong thing try agin')
        gender()

    print('''
    ''')    
gender()
def continues():
    
    con = input('press E to continue to the game: ')
    if con == 'e' or con == 'E':
        pass
    elif con == '' or con == ' ':
        print('you have inputed nothing try agin')
        continues()
    elif con != 'e' or con != 'E':
        print('you have inputed the wrong thing try agin')
        continues()
    print('''
    ''')
continues()
now = time.datetime.now()
hour = now.hour

if hour < 12:
    print("Good morning")
elif hour >= 12 and hour <= 18:
    print("Good afternoon")         
elif hour > 18 and hour < 19: 
    print("Good evening")
else:
    print('Have a nice night.')
    
print(gend,' ',nam,'.Welcome to the reverse game')

print('''
''')
maingame = input('''To proced in the game choose an option:
a.play
b.lern rools
''')
def game():
    if maingame == 'a' or maingame == 'play':
        def main(re):
            return re == re [::-1]
        def main2():
            re = input('pls input a str to see if it can be reversable: ')
            if re == '' or re == ' ':
                print('you have inputed nothing try agin')
                main2()
            ans = main(re)

            if ans:
                print('you have a point')
            else:
                print(re,' cant be reversable tha is no point')
        main2()
    elif maingame =='b' or maingame == 'lern rools':
        print(''' 
        1. Enter word that you think can be read forwards and backwards
        2. if it is correct you will score 1 point.
        3. If it is wrong you get 0 points.''')
    elif maingame == '' or maingame == ' ':
        print('you have inputed nothing try again')
        game()
    elif maingame != 'a' or maingame != 'b':
        print('you have inputed the wrong thing try again')
        game()
game()