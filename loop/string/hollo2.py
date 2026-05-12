# def hollow_square(row):

#     for i in range(row):


#         if i==0 or i==6:

#             for c in range(row):

#                 print(" ^ ",end='')

#         else:

#             print("*",end='')

#             for j in range(row):

#                 print(" ",end='')
                

                
#             print("*",end='')

#             print()



# hollow_square(7)



def hollow_square(row):

    for i in range(row):

        # first and last row
        if i == 0 or i == row - 1:

            for j in range(row):
                print("^", end=" ")

        else:

            print("^", end=" ")

            for j in range(row - 2):
                print(" ", end=" ")

            print("^", end=" ")

        print()


hollow_square(7)
