import sys
''' 
Given a string of n integers, find the longest increasing subsequence in O(n log n) times.
Assumed that a repeatation of same integer is not an increasing sequence.
'''

dp=[]  # dynamic programming array : df[i] stores maximum increasing integer subsequence of length i+1. Stores the one ending with minimum value among all possible strings.   
s=''   # stores the input integer string

'''
Binary search : searches for the last position in dp[] list, where the last character of the element is < x

Input : low, high <- lower and higher indices for range of search in dp[] array
        x <- search element
Output : index position of the last element in dp[] having last char < x.

Example: if dp=['3','35',356'], binarySearch(0,2,'6') returns 1, the index of '35'.

Assumption: dp array should be sorted in ascending order of the last characters of the strings populated in each index.
'''
def binarySearch(low,high,x):
   if low > high:
      return 0        # Not found
   if low+1>=high:
      return low      # found
   if dp[high][-1]<x: # all elements are lower 
      return high
   if dp[low][-1]>=x:  # all elements are higher
      return -1
   
   mid = (low+high)//2
   if dp[mid][-1] < x:# mid is lower, search in range [mid, high]
      return binarySearch(mid,high,x)
   else:              # mid is higher, search in range [low,mid]
      return binarySearch(low,mid-1,x)

'''
LIS: Finds the largest increasing subsequence in an integer string

Input: None.
       Uses global variable : s <- input integer string
Output: length of the largest increasing subsequence
        The largest subsequence is stored in global variable dp.
Logic: This program uses a dynamic programming array, dp. At each index i, dp[i] stores the best increasing sequence with length i+1.
       Best increasing sequence is the one among all increasing sequence of same length, that has the lowest integer at the end (because
       maximum possible numbers can be appended to it).
       Read all integer characters sequentially,
       if it is more than all the last characters of all increasing sequences found so far, then add current char to end of the Longest
         Increasing subsequence found so far, and this becomes the new LIS.
       otherwise, find the largest increasing subsequence, with last character less than the ccurrent integer, and append current integer
         to it. Store it as best LIS for the appropriate length.
         Since the IS (integer sequences) with lowest last integer, are stored in dp, the array dp is sorted in increasing order of the last
         integers of the strings stored in it. Otherwise, if last integer of dp[j] were > last integer of dp[j+1], then the sequence dp[j+1]
         excluding its first integer, could be stored in dp[j].
         So binary search is done to find out the last index in dp, that has last integer lower than current integer read.
         Append current integer to that string, and store it as best. Current integer can be appended to other ISs prior to this, but since
         they have last characters lower than current integer, they are already better thn the new IS could be formed. And current integer
         can not be appended to the ISs in positions after the index found, becuase their last integers are greater than current integer, so
         an increasing sequence can not be formed.
       Once all integers are read, the last non-empty sequence stored in dp will be the longest increasing sequence. 
       
Time complexity: O(n log n)
                 Read each integer sequentially -> O(n), binary search to find last IS lower than current -> O(log n). 
'''
def LIS():
   global dp,s                # Global variables to store dynamic programming array and input string 

   k=0                        # index of the largest string in dp array

   for i in range(len(s)):    # read each integer from the input string
      if i==0 or dp[0]>s[i]:  # if integer read is smallest so far, store it as best IS of length 1
         dp[0]=s[i]
      elif s[i]>dp[k][-1]:    # if integer read is largest so far, append with the LIS to form the new LIS
         dp[k+1]=dp[k]+s[i]
         k += 1
      else:                   # otherwise, perform binary search to find the largest best IS smaller to the current integer, and append to it
         ind=binarySearch(1,k-1,s[i])
         if ind == -1:
            print(dp)
            sys.exit("Something wrong in logic. String ="+s+" Error while processing char="+s[i]+' in position ' + str(i))
         if ind >0:
            dp[ind+1]=dp[ind]+s[i]

   return k+1                 # return largest non-empty index of dp (adding 1 because indexing starts with 0)

'''
Functions prepData and testit are used for testing purpose
'''
def prepData(seq):

   global dp,s

   s=seq
   dp=['' for _ in range(len(s))]   # allocate dynamic programming array to store minimum LIS of all possible lengths 
   return LIS()
   
def testit():
   
   l=prepData('123456789')
   if [l,dp[l-1]]==[9,'123456789']: print('ok')
   else: print("not ok. Length of LIS of 123456789 is ", l, 'check dp=',dp)

   l=prepData('121212')
   if [l,dp[l-1]]==[2,'12']: print('ok')
   else: print("not ok. Length of LIS of 12 is ", l, 'check dp=',dp)

   l=prepData('31276')
   if l==3: print('ok')
   else: print("not ok. Length of LIS of 31276 is ", l, 'check dp=',dp)

   l=prepData('126793548')
   if [l,dp[l-1]] in ([5,'12679'],[5,'12358'],[5,'12348']): print('ok')
   else: print("not ok. Length of LIS of 126793548 is ", l, 'check dp=',dp)
   
''' This is the main function. '''
if __name__ == '__main__':

   # testit()                      # uncomment this line and comment rest of the lines, for testing 

   s=input("Enter a string of integers:")
   dp=['' for _ in range(len(s))]  # allocate dynamic programming array to store best LIS of all possible lengths 
   l=LIS()
   print('Longest increasing subsequence of ', s, ' is ', dp[l-1], ' and length = ',l)
