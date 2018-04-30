import itertools

class Yoda:
    def run(self):
        first = input() 
        second = input()
        N = []
        M = []
        for pair in itertools.zip_longest(list(first)[::-1],list(second)[::-1], fillvalue='0'):
            a,b = pair
            if (a > b):
                N.append(a)
            elif (b > a):
               M.append(b)
            else:
                N.append(a)
                M.append(b)
        firstNumber = ''.join(N[::-1])    
        secondNumber = ''.join(M[::-1])
        if(firstNumber == ''):
            firstNumber = 'YODA'
        else:
            firstNumber = int(firstNumber)
        if ( secondNumber == ''):
            secondNumber = 'YODA'
        else:
            secondNumber = int(secondNumber)
        print(firstNumber)
        print(secondNumber)

if __name__ == '__main__':
    Yoda().run()
