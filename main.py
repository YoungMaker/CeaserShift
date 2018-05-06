import string, random

strs = string.ascii_uppercase #Alphabetic list of uppercase characters

str_freqs = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, .00153, 0.00722, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.0095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074 ]
#relative frequencies of english letters, a-z

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

#counts the frequencies of letters in the given string and puts it in a list
def frequency_count(input_str):
    freq_list = [0]*26

    for char in input_str:
        if char in strs:
            freq_list[ strs.index(char)]+= 1
        else:
            pass # don't count non letters

    return freq_list


#calculates the percentages of the letters based on the frequencies
def prob_count(freq_list, input_size):
    prob_list = [0] * 26

    for i in range(len(freq_list)):
        prob_list[i] = (freq_list[i] / float(input_size))

    return prob_list

def distance_score(prob_list): #this calculates the total error from the distributed frequencies in english
    total_dist = 0.0

    for i in range(len(str_freqs)):
        total_dist += abs(prob_list[i] - str_freqs[i]) #absolute value difference between the frequency percentages of each letter

    return total_dist


if __name__ == '__main__':
    random.seed() #seed the random generator
    #plaintext_file = open("plaintext.txt", "r")
    secret_file = open("secret.txt")
    file_out = open("output.csv", "w")

    secret = secret_file.readline()
    # plaintext = plaintext_file.readline() #read in plaintext
    # secret = shift_by(random.randint(0,26), plaintext) #encrypts with random key 0,26

    file_out.write("?,"+ secret + "\n") #writes out secret message
    file_out.write("Brute Force,\n")

    file_out.write("key, shifted text\n")
    for x in range(1,26): #brute force
        file_out.write( str(x) + "," + shift_by(x, secret) + "\n")

    file_out.write("Frequency analysis,\n")
    file_out.write("frequency distance, key\n")
    scores = [0] * 26
    for z in range(0,26): #try them all for frequency analysis.
        secret_try = shift_by(z, secret) #try a shift
        scores[z] =  distance_score(prob_count(frequency_count(secret_try), len(secret_try))) #caclulate its score and save it
        file_out.write(str(distance_score(prob_count(frequency_count(secret_try), len(secret_try)))) + "," + str(z) + "\n")

    print "" + str(min(scores)) + ", " +str(scores.index(min(scores)))
    print shift_by(scores.index(min(scores)), secret)

    file_out.write(str(min(scores)) + ", " +str(scores.index(min(scores))) + "\n,")
    file_out.write(shift_by(scores.index(min(scores)), secret))
    file_out.write("\n")

    secret_file.close()
    # plaintext_file.close()
    file_out.close()
