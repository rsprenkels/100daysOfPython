class Qsort:
    def sort(self, mylist):
        self.qsort(mylist, 0, len(mylist) - 1)
        return mylist

    def qsort(self, mylist, p_start, p_end):
        if p_start < p_end:
            pi = self.partition(mylist, p_start, p_end)
            self.qsort(mylist, p_start, pi - 1)
            self.qsort(mylist, pi + 1, p_end)

    def partition(self, mylist, p_start, p_end):
        pivot = mylist[p_end]
        i = p_start - 1
        for j in range(p_start, p_end):
            if mylist[j] <= pivot:
                i += 1
                mylist[i], mylist[j] = mylist[j], mylist[i]
        mylist[p_end], mylist[i + 1] = mylist[i + 1], mylist[p_end]
        return i + 1

