class firstIndex:
    def getFirstIndex(self, haystack, needle):
        if needle in haystack:
            lst = haystack.split(needle)
            print(lst)
            ans = len(lst[0])
            return ans
        else:
            return -1


item1 = firstIndex()
print(item1.getFirstIndex("sadbutsad", "sad"))
