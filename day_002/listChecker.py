import itertools

class ListChecker:

    def isConsistent(self, list=[]):
        
        if len(list) <= 1:
            return True
        
        for index, elem in enumerate(list):
            list[index] = ''.join(elem.split())

        for combi in itertools.permutations(list, 2):
            if combi[0].startswith(combi[1]):
                return False
        
        return True
         
