def print_pyramid(rows):
    for i in range(1,rows+1):
        for j in range(i ,rows):
            print(' ', end='')
        for k in range(1,i + 1):
            print('* ', end='')
        print()


print_pyramid(6)