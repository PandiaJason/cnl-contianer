def xor(a, b):
    return ''.join(['0' if i == j else '1' for i, j in zip(a, b)])

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

def checkData(codeword, key):
    remainder = mod2div(codeword, key)
    return remainder

if __name__ == "__main__":
    data = input("Enter binary data to transmit: ")
    key = input("Enter generator polynomial (binary): ")

    print("\nEncoding...")
    codeword = encodeData(data, key)
    print("Transmitted Codeword:", codeword)

    print("\nSimulating Transmission...")
    received = input("Enter received codeword: ")
    result = checkData(received, key)
    if '1' in result:
        print("Error detected in received data.")
    else:
        print("No error detected.")
