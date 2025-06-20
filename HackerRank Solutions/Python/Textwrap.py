import textwrap

def wrap(string, max_width):
    '''

    '''
    # result = ''
    # for i in range(0, len(string)):
    #     if i != 0 and i % max_width == 0:
    #         result += '\n'
    #     result += string[i]
    #
    # return result

    return '\n'.join(textwrap.wrap(string,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)