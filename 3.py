#Task
#Read an integer N. For all non-negative integers i<N, print i**2. See the sample for details.

#Input Format
#The first and only line contains the integer, N .

#Output Format
#Print N lines, one corresponding to each i.
if __name__ == '__main__':
    n = int(input())
    for x in range(n):      
        print (x**2)
