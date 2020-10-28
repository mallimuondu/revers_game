input1 = input("Enter e to add 1:  ")
if input1 == "e":
    squares = []
    a = True
    while a == True:
        squares.append(1)
        print(squares)
        sum = 0
        for num in squares:
            sum += num
        print(sum)
        input1 = input("Do you want to try again:  ")
        if input1 == "yes":
            continue
        else:
            a = False
