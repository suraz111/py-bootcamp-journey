def isPalindrome(x):
    if x < 0:
        return False
    string_x = str(x)
    return string_x == string_x[::-1]
user_input = input("Enter a number: ")
number = int(user_input) #for changing input to integer
print(isPalindrome(number)) #forcheckingpalindrome

