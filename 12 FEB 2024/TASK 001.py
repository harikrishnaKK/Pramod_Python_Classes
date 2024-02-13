#Create a function that checks if a given string is a palindrome
# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
word = str(input("Enter any word is:- "))
ans = isPalindrome(word)

if ans:
    print("This word is an palindrome")
else:
    print("This word is not an palindrome")