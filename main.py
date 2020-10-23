import datetime as time


print('Hello!')
def name():
    global nam
    nam = input('please input your name: ')
    if nam == '' or nam == ' ':
        print('you have inputed nothing try again')
        name()
    else:
        print('Thankyou ',nam)
        print('''
        ''')
name()
def gender():
    global gend
    gend = input('Are you male or lady: ')
    if gend == 'male':
        print('thankyou ',gend,' ',nam)
    elif gend == 'lady':
        print('thankyou ',gend,' ',nam)
    elif gend == ' ' or gend == '':
        print('you have inputed nothing try again')
        gender()
    elif gend != 'male' or con != 'lady':
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
