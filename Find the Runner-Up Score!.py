# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.
#
# Input Format
# # The first line contains n . The second line contains an array A[] of n integers each separated by a space.
#
# Output Format
# # Print the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
#sorts and reverses order of array
    sortArr = sorted(arr)
    sortArr.reverse()
    
#checks for second largest number
    i = 1
    while i <= n:
        if sortArr[i] < sortArr[i - 1]:
            print(sortArr[i])
            break
        else:
            i += 1
    i += 1
