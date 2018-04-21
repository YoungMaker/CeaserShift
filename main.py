import string, random

strs = string.ascii_uppercase


#algorithm based on
#https://stackoverflow.com/questions/14424500/text-shift-function-in-python
def shift_by(shift, inputStr):
    inputStr = inputStr.upper() #shift everything to uppercase
    shiftText = ""
    for char in inputStr:
        if char in strs: #if char is letter
            shiftText += "" + strs[(strs.index(char) + shift) % 26] #shift letter by index + shift mod 26
        else:
            shiftText += "" +  char #char is not letter, simply append it
    return shiftText



if __name__ == '__main__':
    random.seed()
    plaintext_file = open("plaintext.txt", "r")
    file_out = open("output.txt", "w")

    plaintext = plaintext_file.readline()

    file_out.write(shift_by(random.randint(0,26), plaintext))

    plaintext_file.close()
    file_out.close()
