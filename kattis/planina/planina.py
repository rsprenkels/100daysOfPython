class Planina:

    def run(self):
        tot_generations = int(input())
        points = 2
        for gen in range(tot_generations):
            points += (points - 1)
        print (points * points)


if __name__ == '__main__':
    Planina().run()
