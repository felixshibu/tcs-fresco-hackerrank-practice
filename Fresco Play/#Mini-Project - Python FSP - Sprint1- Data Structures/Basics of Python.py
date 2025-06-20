import ast

# Enter your code here. Read input from STDIN. Print output to STDOUT

def numbers(num1, num2, num3, num4):

    arr = [num1, num2, num3, num4]

    '''
    Find the sum of all the numbers and store it in variable sum_of_numbers
    '''

    sum_of_numbers = sum(arr)

    '''
    Find the sum of float numbers among the numbers and store it in variable sum_of_float_numbers
    '''

    sum_of_float_numbers = 0

    for num in arr:
        if isinstance(num, float):
            sum_of_float_numbers += num

    '''
    Find the smallest integer number among the numbers and store it in variable min_number
    '''
    int_arr = []
    for num in arr:
        if isinstance(num, int):
            int_arr.append(num)
    min_number = min(int_arr)

    '''
    Find the count of prime numbers among the numbers and store it in variable prime_count
    '''
    prime_count = 0

    def is_prime(num):
        if num in [0, 1]:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for num in arr:
        if (isinstance(num, int) and is_prime(num)):
            prime_count += 1

    '''
    Check for zeros. If there are zeros present among the numbers, store True else store False in the variable zero_check
    '''

    for num in arr:
        if num == 0:
            zero_check = True
            break
        else:
            zero_check = False

    print(sum_of_numbers)
    print(sum_of_float_numbers)
    print(min_number)
    print(prime_count)
    print(zero_check)


if __name__ == '__main__':
    num1 = ast.literal_eval(input())
    num2 = ast.literal_eval(input())
    num3 = ast.literal_eval(input())
    num4 = ast.literal_eval(input())
    numbers(num1, num2, num3, num4)