import timeit
import numpy as np

# Global variables
a=''                    # first string
b=''                    # second string
d=[]                    # matrix for dynamic programming


'''
Recursive program to return length of the maximum possible substrings of
first m characters of string stored in global variable a, and first n characters of string stores in global variable b.

'''
def getLengthLCS(m,n):
    global a,b,d                   # declare global variables for strings and matrix for dynamic programming
    
    if d[m,n]!=-1:                 # if the length is already calculated and stored by prior recursion steps, 
        return d[m,n]              #  then do not recalculate, just get from matrix of dynamicprogramming
    
    if m==0 or n==0:               # if one of the strings is null, then common string length is 0
        k = 0
    elif a[m-1]== b[n-1]:          # if the last characters of both strings are same, 
        k = 1+getLengthLCS(m-1,n-1)#  then get largest common substring excluding the last characters, and add 1 to it 
    else:                          # otherwise, exclude last char from either of the string and get largest common substring with the other, take string with maximum length
        k = max(getLengthLCS(m-1,n),getLengthLCS(m,n-1))

    d[m,n]=k                       # store LCS value for future recursions to pick up 
    return k

'''
Find out the largest common string from the matrix of dynamic programming

Logic: In the dynamic programming matrix (filled up by function getLengthLCS), start travelling from
       bottom right corner.
       If value of a position is > value of its top-left diagonal element,
          then this value os populated when last element of two strings are equal (1+getLengthLCS(m-1,n-1))
          so this position is part of largest common string.
       otherwise, the position is filled up by code 'max(getLengthLCS(m-1,n),getLengthLCS(m,n-1))', so go
          to left or up neighbour depending on which one is maximumum, and do not include current position
          in LCS.
       This way travel from right-bottom to left-up direction, until the boundary of the matrix reached,
       or a value 0 is read in a position, which means no match found on or before that position.
    
'''
def getStringLCS(m,n):
    
    global a,b,d                        # declare global variables for strings and matrix for dynamic programming
    s=''                                # stores LCS
    i,j=m,n                             # row and column variables to travel in matrix, initially set to right-bottom corner

    while i>=0 and j>=0 and d[i,j] > 0: # travel until lower boundary for row or column reached, or all no more positive values (matches)  
        if d[i,j]==d[i-1,j-1]:          # if element = left-up diagonal element 
            i,j=i-1,j-1                 #   so travel in diagonal direction
        elif d[i,j]==d[i,j-1]:          # else if top neighbour is same, travel top
            j=j-1
        elif d[i,j]==d[i-1,j]:          # if diagonal and top are less, but left neighbor is same, travel left
            i=i-1
        else:                           # if diagonal, top and left elements are all smaller than the current position value, then its part of LCS
            s=a[i-1]+s                  # add in the beginning of LCS, as travelling backward
    #        print(i,j,a[i-1])
            i,j=i-1,j-1
    return s

def getLargestCommonSubstring(s,t):

    global a,b,d                        # declare global variables for strings and matrix for dynamic programming
    a,b=s,t                             # set global variables for strings to user enteres strings

    d=np.full((len(a)+1,len(b)+1),fill_value=-1,dtype=int) # initialise matrix for dynamic programming to all -1, and of size len(1st str)*len(2nd str)
    d[:,0]=0                            # set first column and row to 0, as base condition : LCS(0,k)=0=LCS(k,0)
    d[0,:]=0

    m=len(a)
    n=len(b)

    l=getLengthLCS(m,n)                 # get length by calling getLengthLCS with length of 1st and 2nd strings

    return l,getStringLCS(m,n) 

'''
Code for test at mass level, after making any change
Should see 'ok' in stdout for all test cases, if program works fine
'''
def testit():
     if getLargestCommonSubstring('a','a')== (1,'a'): print('ok')
     else: print('Not ok')
     if getLargestCommonSubstring('a','v')== (0,''): print('ok')
     else: print('Not ok')
     if getLargestCommonSubstring('ab','a')== (1,'a'): print('ok')
     else: print('Not ok')
     if getLargestCommonSubstring('a','ba')== (1,'a'): print('ok')
     else: print('Not ok')
     if getLargestCommonSubstring('abcd','vbrdf')== (2,'bd'): print('ok')
     else: print('Not ok')
     if getLargestCommonSubstring('DikstrasAllElephantAnts','LoydWarshallAntsElephantsTogetherWalk') in [(13,'asllElephants'),(13,'asllElephantt')]: print('ok')
     else: print('Not ok',' ',getLargestCommonSubstring('DikstrasAllElephantAnts','LoydWarshallAntsElephantsTogetherWalk'))
     if getLargestCommonSubstring('MZJAWXU','XMJYAUZ')== (4,'MJAU'): print('ok')
     else: print('Not ok')
     if getLargestCommonSubstring('AGGTAB','GXTXAYB')== (4,'GTAB'): print('ok')
     else: print('Not ok')

   
if __name__=='__main__':
    
     a=input('First string:')           # 1st user input
     b=input('Second string:')          # 2nd user input
     l,s=getLargestCommonSubstring(a,b) # get length and string for the LCS
     print('Length of a largest common substring between ', a, ' and ',b, ' is ', l)
     if l>0:
         print('And it is ',s)

     #testit()                          # mass testing -> comment out previous lines and uncomment this line to perform mass testing after a change.   
