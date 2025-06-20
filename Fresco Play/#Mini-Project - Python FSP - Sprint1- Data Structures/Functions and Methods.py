import ast

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Write the function list_oper that takes two list as input.

Function should return a string after performing the operations specified below
 - Check for the squares and cubes of elements in list1 is present in list2
 - Return "Squares and Cubes are present" if squares and cubes of all elements in list1 are present in list2.
 - Return "Squares are only present" if squares of all elements in list1 are only present in list2.
 - Return "Cubes are only present" if cubes of all the elements in list1 are only present in list2.
 - Return "No such pattern is present" if there are squares and cubes of any element in list1 is not present in list2
'''


def list_oper(list1, list2):
    squares_present = all(x ** 2 in list2 for x in list1)
    cubes_present = all(x ** 3 in list2 for x in list1)

    if squares_present and cubes_present:
        return "Squares and Cubes are present"
    elif squares_present:
        return "Squares are only present"
    elif cubes_present:
        return "Cubes are only present"
    else:
        return "No such pattern is present"


'''
Write the function amstrong which takes two numbers(num1,num2) as input. Function should return the list of amstrong numbers between num1 and num2

Example : [0,1,..]
'''


def amstrong(num1, num2):
    result = []

    for num in range(num1, num2):
        num_str = str(num)
        digit_list = []

        for digit in num_str:
            digit_list.append(digit)

        digits_sum = 0

        for digit in digit_list:
            digits_sum += int(digit) ** len(num_str)

        if (digits_sum == num):
            result.append(num)

    return result


'''
Write the function string_oper which takes a string as input and return another string after removing words that have characters repeated

Input : "This is an example"
Output : "This is an"
'''


def string_oper(string1):
    result = []
    for word in string1.split(' '):
        for char in word:
            if word.count(char) > 1:
                break
        else:
            result.append(word)
    return ' '.join(result)


'''
Write a function string_reverse which takes a string as input and return another string with each word in reversed order.

Example : "START OF THE PROJECT"
Output :  "TRATS FO EHT TCEJORP"
'''


def string_reverse(string2):
    result = []
    for word in string2.split(' '):
        result.append(word[::-1])

    return ' '.join(result)


if __name__ == '__main__':
    list1 = ast.literal_eval(input())
    list2 = ast.literal_eval(input())
    num1 = ast.literal_eval(input())
    num2 = ast.literal_eval(input())
    string1 = input()
    string2 = input()
    print(list_oper(list1, list2))
    print(amstrong(num1, num2))
    print(string_oper(string1))
    print(string_reverse(string2))