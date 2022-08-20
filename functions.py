from random import randint


def mul(num):
    for i in range(1,11):
        print('{} x {} = {}'.format(i,num,i*num))

def sumOfTwoStr(str1, str2):
    print('test two strings')
    s1=str1.replace(' ','')
    s2=str2.replace(' ','')

    result=''

    for char in s1:
        if s2.find(char) > -1 and result.find(char) < 0 :
            result +=char
    
    return len(result)

def guessNum(num):
    x = randint(1,10)
    if num < x :
        print('Your number is too small!')
    if num > x :
        print('Your number is too big!')
    if num==x:
        print('You are SUPER! Your number is correct!')


# mul(12)
# num = int(input('Please guess the number between 1 and 10:'))
# guessNum(num)

x = sumOfTwoStr('beer hola', 'peer lalala')
print(x)