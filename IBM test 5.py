# Pascal's Triangle Centered Printing

def pascal_triangle_centered(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1) # initialize row with 1s
        for j in range(1, i): # the range is capped by i, this allows the last value of the current row to remain 1
            row[j] = triangle[i-1][j-1] + triangle[i-1][j] # i-1 is the previous row
        triangle.append(row)

    for i in range(n):
        print(" " * (n - i - 1), end="") # n-i-1 = center alignment
        print(" ".join(str(x) for x in triangle[i])) 

pascal_triangle_centered(10)