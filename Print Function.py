# Read an integer N.
# # Without using any string methods, try to print the following:
# # 123...N
# # Note that "..." represents the values in between.
#
# Input Format
# # The first line contains an integer .
#
# Output Format
# # Output the answer as explained in the task.

if __name__ == '__main__':
    n = int(input())
    numList = []
    while n !=0:
        numList.append(n)
        n -= 1
    numList.sort()
    for i in numList:
        print(i, end="")