def get_encoded_str(root, data):
    '''Encoded string'''
    codes = get_codes(root)
    compressed_data = []
    for d in data:
        compressed_data.append(codes[d])
    return ''.join(compressed_data)


def get_decoded_str(root, encoded_str):
    ''' Decode encoded string '''
    decoded_data = []
    current = root
    for code in encoded_str:
        if code == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            char = current.char
            decoded_data.append(char)
            current = root
    return ''.join(decoded_data)


def get_codes(root):
    current = root
    codes = {}
    code = []
    recursive(root, codes, code)
    return codes


def recursive(current, codes, code):
    if current.is_leaf():
        key = current.char
        codes[key] = ''.join(code)
        return

    if current.left:
        code.append('0')
        recursive(current.left, codes, code)
        code.pop()

    if current.right:
        code.append('1')
        recursive(current.right, codes, code)
        code.pop()



