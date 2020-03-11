'''
Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.
'''

if __name__ == '__main__':
    print(*range(1, int(input())+1), sep='')
