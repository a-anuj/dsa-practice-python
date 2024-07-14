class Sum:
    def find_sum(self, lst, n):
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i == j:
                    continue
                elif lst[i]+lst[j] == n:
                    return i+1, j+1
                else:
                    continue


sum1 = Sum()
ans = sum1.find_sum([3, 2, 4], 6)
print(ans)
