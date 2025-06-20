if __name__ == '__main__':
    N = int(input())
    li = []
    main_list = []
    for i in range(0, N):
        command = input()
        li = command.split(" ")
        if (li[0] == "insert"):
            main_list.insert(int(li[1]), int(li[2]))
        elif (li[0] == 'print'):
            print(main_list)
        elif (li[0] == 'remove'):
            main_list.remove(int(li[1]))
        elif (li[0] == 'append'):
            main_list.append(int(li[1]))
        elif (li[0] == 'sort'):
            main_list.sort()
        elif (li[0] == 'pop'):
            main_list.pop()
        elif (li[0] == 'reverse'):
            main_list.reverse()
