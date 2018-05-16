class Greedilyincreasing:

    def run(self):
        N = int(input())
        permu = list(map(int, input().split()))
        len_permu = len(permu)
        gis = []
        cur_max = permu[0]
        gis.append(cur_max)
        # print(' '.join(str(x) for x in permu))
        check_index = 1
        while check_index < len_permu:
            if permu[check_index] > cur_max:
                gis.append(permu[check_index])
                cur_max = gis[-1]
            check_index += 1
        print(len(gis))
        print(' '.join(str(x) for x in gis))

if __name__ == '__main__':
    Greedilyincreasing().run()