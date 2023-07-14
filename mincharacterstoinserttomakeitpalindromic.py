def minCharsforPalindrome(s):

 

    i , j , trim = 0,len(s)-1,len(s)-1

    cnt = 0

    while i<j:

 

        

        if s[i]==s[j]:

            i+=1

            j-=1

 

       

        else:

            cnt += 1

            i = 0

            trim -=1

            j = trim

 

    return cnt