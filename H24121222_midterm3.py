def parse_matrix(input_str):
    """Parses the input string into a dictionary-based matrix."""
    rows = input_str.strip().split('|')
    matrix = {}
    for i, row in enumerate(rows):
        # Replace non-standard hyphens with standard hyphens
        row = row.replace('‐', '-').replace('–', '-').replace('—', '-')
        elements = list(map(int, row.split(',')))
        for j, element in enumerate(elements):
            matrix[(i, j)] = element
    return matrix

def multiply_matrices(U, V, n):
    """Multiplies two n x n matrices U and V stored as dictionaries."""
    M = {}
    for i in range(n):
        for j in range(n):
            M[(i, j)] = sum(U.get((i, k), 0) * V.get((k, j), 0) for k in range(n))
    return M

def matrix_to_string(matrix, n):
    """Converts the dictionary-based matrix to a string with square brackets for printing."""
    rows = []
    for i in range(n):
        row = [matrix.get((i, j), 0) for j in range(n)]
        row_str = '[' + ', '.join(map(str, row)) + ']'
        rows.append(row_str)
    return '\n'.join(rows)

def main():
    try:
        U_str = input("Enter matrix U: ").strip()
        V_str = input("Enter matrix V: ").strip()
        
        U = parse_matrix(U_str)
        V = parse_matrix(V_str)
        
        # Assuming both matrices are square and of the same size
        n = int(len(U) ** 0.5)
        
        M = multiply_matrices(U, V, n)
        
        print("M = U x V")
        print(matrix_to_string(M, n))
    
    except ValueError:
        print("Invalid input format. Please ensure you enter the matrices correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

