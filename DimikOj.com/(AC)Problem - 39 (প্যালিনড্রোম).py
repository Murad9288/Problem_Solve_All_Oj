for _ in range(int(input())):
    n = str(input())
    if n == n[::-1]:
        print("Yes! It is Palindrome!")
    else:
        print("Sorry! It is not Palindrome!")
