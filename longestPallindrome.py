#!/usr/bin/env python
# coding: utf-8

import sys    # for system exit

dp=[]         # used for dynamic programming. dp[i,j] stores the length and a longest palindrome possible with the sequence starting at i and ending at j positions in input string
inp=''        # stores input string
inp_count=[[0,[]] for _ in range(52)] # stores count and index of recurrences of each characters in the input string

'''
Returns the index of each input char in inp_count array
'''

def getNum(c):
    if c<'a':
        return ord(c)-ord('A')    # indices 0 to 25 for capital letters
    else:
        return 26+ord(c)-ord('a') # indices 26 to 51 for capital letters

'''
Counts recurrence of each distinct characters in input and their positions. Stores in inp_count.
Also populates dp table with palindromes of single character and consecutive repeatitive characters.
'''

def checkPositions():
    global dp,inp,inp_count
    N=len(inp)                  # length of input
    dp=[[[0,''] for _ in range(N)] for _ in range(N)] # dynamic programming array size n x n, initialised with empty palindromes
    for i in range(N):
        dp[i][i]=[1,inp[i]]     # single charater palindromes
        if i==0:
            rStart=0            # used to find repeating char sequence
            rEnd=0
        elif inp[i]!=inp[i-1]:  # if no repeat, store previous repeat char in dp
            dp[rStart][rEnd]=(rEnd-rStart+1,inp[rStart:rEnd+1])
            rStart=i
            rEnd=i
        else:
            rEnd += 1           # if repeat, increase count
        
        ind=getNum(inp[i])      # get index of current char in inp_count array
        inp_count[ind][0] += 1  # increase count
        inp_count[ind][1].append(i) # store position

'''
Identifies longest palindrome within start and end positions of a given sequence.
'''

def LPS(start,end):
    global dp,inp,inp_count
    
    if start>end or start <0 or end<0:  # inconsistent input variables
        return 0,''
    if dp[start][end][0]>0:             # palindrome details are already stored in dynamic programming array, take from there and return
        return dp[start][end]
    
    maxPalindrome=[1,inp[start]]        # used to store the longest palindrome in the current range
    for i in range(start,end+1):        # loop for each input char in current range
        index=getNum(inp[i])
        if inp_count[index][0]>1:       # if char repeats within current range
            positions=inp_count[index][1] # get all repeating positions 
            for j in positions[positions.index(i)+1:]: # loop for each repeat positios
                if j>end:               # process only if repeat position is within current range 
                    break
                length,palindrome=LPS(i+1,j-1) # current and repeat positions are the start and end chars of this palindrome. Get largest palindrome excluding them and add start, end to form largest palindrome  
                length += 2
                if length > maxPalindrome[0]: # store the largest ones only
                    maxPalindrome=[length,inp[i]+palindrome+inp[j]]
    dp[start][end]=maxPalindrome        # store palindrome in dynamic programming array for future reference
    return dp[start][end]

'''
Main program. Receives input string from stdin, and prints the largest subsequence palindrome. 
'''

if __name__=='__main__':
    inp=input("Enter an alphabetic string:")
    if inp.isalpha()==False:
        sys.exit("Non alphabetic characters entered.")
    checkPositions()  # first pass to store positions of unique characters
    N=len(inp)-1
    LPS(0,N)          # use the positions stored abive and identify one largest subsequence palindrome
    print("Longest palindromic subsequene of ", inp, "is ",dp[0][N][1])
