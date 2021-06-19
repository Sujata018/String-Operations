''' 
Given a string of n integers, find the longest increasing subsequence in
O(n log n) times.
Assumed that a repeatation of same integer is not an increasing sequence.
'''

dp=[]  # dynamic programming array : stores maximum increasing integer subsequence possible starting with and including the integer is the current position of input integer string 
s=''   # stores the input integer string
N=0    # stores length of s

def LIS(n,runningSequence):
   global dp,s,N

   if n>=N:              # if all integers are read
      return 0,''        #  empty sting of 0 length possible from reading further 
   if runningSequence > '' and s[n] <= runningSequence[-1]:
      return LIS(n+1,runningSequence)
   else:
      if dp[n]==[0,'']:     # if dp table is not filled up, calculate
   
         l1,subseq1=LIS(n+1,runningSequence+s[n]) # get length, max increasing subsequence if current integer is part of it
         l1 += 1                                    # add current integer to the result before retirning to parent recursion 
         subseq1 = s[n] + subseq1
         dp[n]=[l1,subseq1]                         # fill up dp table for further recursions to use

      l2,subseq2=LIS(n+1,runningSequence)           # get maximum subsequence excluding the current integer

      if dp[n][0]>=l2:                              # return the larger one to parent program
         l=dp[n][0]
         subseq=dp[n][1]
      else:
         l=l2
         subseq=subseq2

   return l,subseq

def prepData(seq):

   global N,dp,s

   s=seq
   N=len(s)
   dp=[[0,''] for _ in range(N+1)]
   dp[N]=[0,'']
   return LIS(0,'')
   
def testit():
   
   l,seq=prepData('123456789')
   if [l,seq]==[9,'123456789']: print('ok')
   else: print("not ok. Length of LIS of 123456789 is ", l)

   l,seq=prepData('121212')
   if [l,seq]==[2,'12']: print('ok')
   else: print("not ok. Length of LIS of 12 is ", l)

   l,seq=prepData('31276')
   if l==3: print('ok')
   else: print("not ok. Length of LIS of 12 is ", l)
   
''' This is the main function. '''
if __name__ == '__main__':

   #testit() 

   s=input("Enter a string of integers:")
   N=len(s)
   dp=[[0,''] for _ in range(N+1)]
   dp[N]=[0,'']
   length,subs=LIS(0,'')
   print('Longest increasing subsequence of ', s, ' is ', subs, ' and length = ',length)
