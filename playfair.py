def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)
    for i in range(65, 91):  # A-Z
        if chr(i) not in matrix and chr(i) != 'J':
            matrix.append(chr(i))
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    raise ValueError(f"Character '{char}' not found in Playfair matrix.")

def preprocess_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    processed = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            processed += a + 'X'
            i += 1
        else:
            processed += a + b
            i += 2
    if len(processed) % 2 != 0:
        processed += 'X'
    return processed

def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    text = preprocess_text(text)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            result += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def playfair_decrypt(text, key):
    matrix = generate_matrix(key)
    text = text.upper().replace(" ", "").replace("J", "I")
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            result += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result
