class Planina:

    def run(self):
        num_cases = int(input())
        for case in range(num_cases):
            beats, period = input().split()
            beats = int(beats)
            period = float(period)
            bpm_min = (beats - 1) * 60 / period
            bpm_nom = beats * 60 / period
            bpm_max = (beats + 1) * 60 / period
            print("{:.4f} {:.4f} {:.4f}".format(bpm_min, bpm_nom, bpm_max))
        return 0


if __name__ == '__main__':
    Planina.run()
