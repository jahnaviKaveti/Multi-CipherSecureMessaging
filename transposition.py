def transposition_encrypt(text, key):
    columns = ['' for _ in range(key)]
    for index, char in enumerate(text):
        columns[index % key] += char
    return ''.join(columns)

def transposition_decrypt(text, key):
    n_rows = len(text) // key
    extra = len(text) % key
    cols = []
    k = 0
    for i in range(key):
        col_len = n_rows + 1 if i < extra else n_rows
        cols.append(text[k:k+col_len])
        k += col_len
    result = ''
    for i in range(n_rows + 1):
        for j in range(key):
            if i < len(cols[j]):
                result += cols[j][i]
    return result