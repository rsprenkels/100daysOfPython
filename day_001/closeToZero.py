class CloseToZero:

    def answer(self, list):
        smallest = list[0]
        for item in list[1:]:
            if abs(item) < abs(smallest):
                smallest = item
            if abs(item) == abs(smallest):
                smallest = max(item, smallest)    
        return smallest
        