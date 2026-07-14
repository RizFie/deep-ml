def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    result = []
    col = 0;
    for j in range(len(a[col])):
        print(f'j: {j}')
        new_row = []
        for i in range(len(a)):
            print(a[i][j])
            new_row.append(a[i][j])
        result.append(new_row)
    print(result)
    return result
