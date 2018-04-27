import itertools

class Anagram:

    def generate(self, input):
        allCombinations = []
        for combi in itertools.permutations(input):
            print(combi)
            allCombinations.append(''.join(combi))
        return allCombinations
