# palindrome numbers

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def main():
    def test():
        assert isPalindrome(12321) == True
        assert isPalindrome(12345) == False
        assert isPalindrome(123321) == True
        assert isPalindrome(123456) == False
        assert isPalindrome(123454321) == True
        assert isPalindrome(123456789) == False
    test()
    num = int(input("Enter a multi digit number: "))
    if isPalindrome(num):
        print(f"{num} is a palindrome number")
    else:
        print(f"{num} is not a palindrome number")


main()
