def vestigium():
    t = int(input())
    for case in range(t):
        matrix_Size = int(input())

        matrix = []

        for i in range(matrix_Size):
            arr = list(map(int, input().split()))
            matrix.append(arr)

        diagonal = 0
        x = 0
        for row in matrix:
            diagonal += row[x]
            x +=1
        #return diagonal

        count_of_rows = row_counter(matrix)
        new_matrix = transpose(matrix)
        count_of_column = row_counter(new_matrix)
        print("Case #{}: {} {} {}".format(case+1, diagonal, count_of_rows, count_of_column))


def row_counter(mm):
    count = 0
    for i in range(len(mm)):
        if len(mm[i]) != len(set(mm[i])):
            count += 1
    return count


def transpose(m):

    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    tr = [row for row in rez] 
    return tr

vestigium()