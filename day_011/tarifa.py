class Tarifa:

    def run(self):
        X = int(input())
        N = int(input())
        usage = []
        
        for u in range(N):
            usage.append(int(input()))

        print(X * (N+1) - sum(usage))


if __name__ == '__main__':
    Tarifa().run()
