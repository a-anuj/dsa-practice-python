class palindrome:
    def check_palindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


one = palindrome()
print(one.check_palindrome(-121))
