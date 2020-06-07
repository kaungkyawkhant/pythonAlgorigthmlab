def getConvertedString(letter, key):
    newLetter = ord(letter) + key
    return chr(newLetter) if newLetter <= 122 else chr(96 + newLetter % 122)


def caesarEncryptor(string, key):
    resultString = []
    newKey = key % 26
    for char in string:
        resultString.append(getConvertedString(char, newKey))
    return "".join(resultString)
print(caesarEncryptor('orange', 145))