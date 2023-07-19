def median(matrix: [[int]], m: int, n: int) -> int:

    spreadMatrix = []

    # Transfer the elements
    for i in range(len(matrix)):
    
        for j in range(len(matrix[i])):
        
            spreadMatrix.append(matrix[i][j])
        
    

    # Sort to find the median
    spreadMatrix.sort()

    # Return the middle element
    return spreadMatrix[m * n // 2]