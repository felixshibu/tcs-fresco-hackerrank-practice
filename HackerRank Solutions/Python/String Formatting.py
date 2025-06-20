def print_formatted(number):
    # your code goes here
    for i in range(0,number):
        print("{0}\t{1:o}\t{1:X}\t{1:b}".format(i,i,i,i))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)