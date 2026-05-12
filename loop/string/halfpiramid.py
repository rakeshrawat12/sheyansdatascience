def HalfPiramiD(rows):
    for i in range(rows):

        for c in range(i+1):

            print("^",end='')

        print()


HalfPiramiD(6)



def ultaHalfPyramid(rows):

    for i in range(rows):

        for c in range(rows - i):

            print("^", end=' ')

        print()


ultaHalfPyramid(6)



def NumberPiramiD(rows):
    for i in range(rows):

        for c in range(1,i+1):

            print(c,end=' ')

        print()


NumberPiramiD(6)



print()
def NumberultaHalfPyramid(rows):

    for i in range(rows):

        for c in range(1,rows - i):

            print(c,end=' ')

        print()


NumberultaHalfPyramid(6)



def SpaceStar(rows):

    for row in range(rows):

        # spaces
        for space in range(rows - row - 1):
            print(" ", end='')

        # stars
        for star in range(row + 1):
            print("*", end=' ')

        print()


SpaceStar(5)







