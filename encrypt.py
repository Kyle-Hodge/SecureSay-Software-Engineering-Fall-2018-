def encrypt(message):
    result = ''
    for i in range(0, len(message)):
	result = result + chr(ord(message[i]) - 2)
    return result

def decrypte(message):
    for i in range(0, len(message)):
	result = result + chr(ord(message[i]) + 2)
    return result
 

test_str = "hello world"
print encrypt(test_str)
