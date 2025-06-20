# Enter your code here. Read input from STDIN. Print output to STDOUT
def data_oper(string1, string2):
    '''
    Split the string string1 with whitespace as delimiter
    Remove the words that contain characters that are not alphabets
    Remove the words whose length is less than 3
    Convert first letter of each word in to Upper case
    Store it in variable list1
    Type of list1 - List
    '''

    list1 = []

    def is_valid(word):
        for c in word:
            if not c.isalpha():
                return False
        return True

    for word in string1.split(' '):
        if len(word) >= 3 and is_valid(word):
            list1.append(word.capitalize())

    '''
    Split the string string2 with whitespace as delimiter
    Remove the words that contain characters that are not alphabets
    Remove the words whose length is less than 3
    Convert first letter of each word in to Upper case
    Store it in variable list2
    Type of list2 - List
    '''

    list2 = []

    for word in string2.split(' '):
        if len(word) >= 3 and is_valid(word):
            list2.append(word.capitalize())

    '''
    Concatinate the lists list1,list2 and store it in variable list3
    Type of list3 - List
    '''

    list3 = list1 + list2

    '''
    Find the count of each word in the list list3 and store it in variable count_dictionary
    Type of count_dictionary - Dictionary
    Keys have to be words
    Dictionary must be ordered based on Keys
    '''

    count_dictionary = {}

    for word in list3:
        if word not in count_dictionary:
            count_dictionary[word] = 1
        else:
            count_dictionary[word] += 1

    count_dictionary = dict(sorted(count_dictionary.items()))

    '''
    Find the unique words from words of list3 and store it in variable list3_uni
    Type of list3_uni - list
    list3_uni must be sorted in ascending order
    '''

    list3_uni = sorted(list(set(list3)))

    '''
    Find the common words in list1,list2 and store it in variable common_tuple
    Type of common_tuple - tuple
    Words have to unique and sorted in ascending order
    If there are no common words in list1,list2 store an empty tuple
    '''

    common_tuple = ()
    common_set = set()

    for word in list1:
        if word in list2:
            common_set.add(word)

    common_tuple = tuple(sorted(common_set))

    '''
    Find the words of list3 that ends with 's' and store it in variable ends_with
    Type of ends_with - tuple
    Words have to be unique and sorted in ascending order
    If there are no words in list3 that ends with 's', store an empty tuple
    '''

    ends_with = ()
    ends_with_set = set()

    for word in list3:
        if word[len(word) - 1] == 's':
            ends_with_set.add(word)

    ends_with = tuple(sorted(ends_with_set))

    print(list3)
    print(count_dictionary)
    print(list3_uni)
    print(common_tuple)
    print(ends_with)


if __name__ == '__main__':
    string1 = input()
    string2 = input()
    data_oper(string1, string2)