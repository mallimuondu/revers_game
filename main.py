def main(re):
    return re == re [::-1]
re = input('pls input a str to see if it can be reversable: ')
ans = main(re)

if ans:
    print('you have a point')
else:
    print(re,' cant be reversable tha is no point')
