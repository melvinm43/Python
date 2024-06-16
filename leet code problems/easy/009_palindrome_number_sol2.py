def isPalindrome(num):
    if num < 0: return False
    div =1
    while num >=10*div:
        div*=10
    while num:
        if (num//div != num%10): return False
        num = (num % div)//10
        div=div/100
    return True



print(isPalindrome(1221))
