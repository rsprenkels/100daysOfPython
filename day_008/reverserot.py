class Reverserot:

    def run(self):
        code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
        nextline = input().split()
        rotation = int(nextline[0])
        while (rotation > 0):
            message = nextline[1][::-1]
            coded = []
            for char in message:
                coded.append(code[(code.find(char) + rotation) % len(code)])
            print(''.join(coded))
            nextline = input().split()
            rotation = int(nextline[0])

if __name__ == '__main__':
    Reverserot().run()
