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
    file_out = open("output.csv", "w")

    plaintext = plaintext_file.readline()
    secret = shift_by(random.randint(0,26), plaintext)

    file_out.write( "?,"+ secret + "\n")

    for x in range(1,26):
        file_out.write( str(x) + "," + shift_by(x, secret) + "\n")


    plaintext_file.close()
    file_out.close()
