num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = []

def even():
    for i in num1:
        if i % 2 == 0:
            num2.append(i)
    print(num2)

even()