class AnotherSort:
    def sort(self, mylist):
        magic = 'secretA'
        self.qsort(mylist, 0, len(mylist) - 1)
        return mylist

    def qsort(self, mylist, a, b):
        if a < b:
            pi = self.partition(mylist, a, b)
            self.qsort(mylist, a, pi - 1)
            self.qsort(mylist, pi + 1, b)

    def partition(self, mylist, a, b):
        pivot = mylist[b]
        i = a - 1
        for j in range(a, b):
            if mylist[j] <= pivot:
                i += 1
                mylist[i], mylist[j] = mylist[j], mylist[i]
        mylist[b], mylist[i + 1] = mylist[i + 1], mylist[b]
        return i + 1