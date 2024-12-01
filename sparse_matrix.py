# Sparse matrix- In which the zeros in the element are 
#  more than the whole element in the matrix

# Algorithm

# Declare and initialize a two-dimesional array a.
# Calculate the number of rows and columns present in the 
#   given array.
# Loop through the array and count the number of zeroes present
#  in the given array and store in the variable count.
# Calculate the size of the array by multiplying the number
#   rows with many columns of the array.
# If the count is greater than size/2, given matrix is the
#   sparse matrix, That means, most of the elements of the 
#   array are zeroes.
# Else, the matrix is not a sparse matrix.

# a=[
#     [4,0,4],
#     [9,0,0],
#     [0,1,0]
# ]
# count =0
# rows=len(a)
# cols=len(a[0])
# size=rows*cols
# for i in range(0,rows):
#     for j in range(0,cols):
#         if a[i][j]==0:
#             count+=1
# if (count>(size/2)):

#     print("Given matrix is a sparse matrix.")
# else:
#     print("Given matrix is not a sparse matrix.")

def input_matrix():
    matrix = []
    print("Enter the elements of the 3x3 matrix:")

    for i in range(3):
        row = []
        for j in range(3):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix

# Call the function to input the matrix
my_matrix = input_matrix()

# Print the entered matrix
print("\nYou entered the following matrix:")
for row in my_matrix:
    print(row)

            