0x07. Rotate 2D Matrix By Marshal Zvinoira

# Rotate 2D Matrix

## Description
This project provides a function to rotate a given n x n 2D matrix 90 degrees clockwise in place.

## Function
`rotate_2d_matrix(matrix)`

### Parameters
- `matrix`: A list of lists where each sublist represents a row of the matrix.

### Returns
- None: The matrix is modified in place.

## Usage
You can test the function using the provided `main_0.py` script:

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

