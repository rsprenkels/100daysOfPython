class Ostgotska:

    def run(self):
        wordlist = input().split()
        words_with_ae = 0
        for word in wordlist:
            if word.find('ae') >= 0:
                words_with_ae += 1
        if (words_with_ae / len(wordlist)) >= 0.40:
            print('dae ae ju traeligt va')
        else:
            print('haer talar vi rikssvenska')


if __name__ == '__main__':
    Ostgotska.run()