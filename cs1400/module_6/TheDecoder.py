dkey = 0

while True:
    try:
        print("Please enter the key used to decrypt the file.")
        dkey = int(input())
        break
    except ValueError:
        print("Please enbter a number.")
        print("Please try again.")

while True:
    try:
        print("Please enter the file you would like to decrypt.")
        fileNmae = input()

        f = open(fileName, 'r')
        
        decryptedFile = open('decrypted.txt', 'w')
        for line in f:
            for i in range(len(line)):
                letter = line[i]
                chValue = ord(letter)
                chValue -= dkey
                letter = chr(chValue)
                decryptedFile.write(letter)
        break                
            
    except FileNotFoundError:
        print('File does not exist. Please enter the correct  file name.')
    except:
        print('Error ocurred')
print('File was decrypted to decrypted.txt')
f.close()
decryptedFile.close()