class Dicegame:

    def run(self):
        gunnar = sum(list(map(int, input().split())))
        emma = sum(list(map(int, input().split())))

        if (emma > gunnar):
            print('Emma')
        elif (gunnar > emma):
            print('Gunnar')
        else:
            print('Tie')

if __name__ == '__main__':
    Dicegame().run()
