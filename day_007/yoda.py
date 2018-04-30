import itertools

class Yoda:

    def printres(self, theRes):
        nr = ''.join(theRes[::-1])
        if (nr == ''):
            print('YODA')
        else:
            print(int(nr))

    def run(self):
        first, second  = input(), input()
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

        Yoda.printres(self, N)
        Yoda.printres(self, M)

if __name__ == '__main__':
    Yoda().run()
