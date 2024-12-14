
sentence = input("Enter your sentence: ")
shift = int(input("Enter the shift: "))


result = ""


for i in sentence:
    if i.isalpha(): #this condition checks if i is char
        if i.islower(): #Ceaser cipher for lower_case letters
            stayInAlphabet = ord(i) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            elif stayInAlphabet < ord('a'):
                stayInAlphabet += 26
        elif i.isupper(): #Ceaser cipher for upper_case letters
            stayInAlphabet = ord(i) + shift
            if stayInAlphabet > ord('Z'):
                stayInAlphabet -= 26
            elif stayInAlphabet < ord('A'):
                stayInAlphabet += 26
        
        finalLetter = chr(stayInAlphabet)
        result += finalLetter
    else:
        result += i  

print("Result: ", result)
