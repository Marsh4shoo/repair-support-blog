#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        prev_row = triangle[i - 1]
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle

# Example usage
if __name__ == "__main__":
    n = 5  # Example number of rows
    print(pascal_triangle(n))

