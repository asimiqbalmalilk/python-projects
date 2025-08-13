def cipher(txt, shift_amount, mode):
    result  = ""
    if mode.lower() == 'decrypt':
        shift_amount = -shift_amount        # reverse the shift for decryption
    for letter in txt:
        lower = letter.lower()      #converting first each of the letters into lower-case
        if letter.isalpha():
            new_char = ord(lower) + shift_amount        # adding shift to each character of entered name
            if new_char > ord('z'):
                new_char -= 26      # wrapping back
            elif new_char < ord('a'):
                new_char += 26      # incase of negative shifts
            new_char = chr(new_char)    # converting the result back to orignal string form
            if letter.isupper():
                new_char = new_char.upper()     # if a given character was initially uppercase we convert it back to it's original case
            result += new_char
        else:
            result += letter        # add every other item simply to result if it's not an alphabet
    return result

# Main programme
def main():
    mod = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt:' ")
    text = input("Enter your message here (1-25): ")
    shift = int(input("Enter the shift amount: "))
    output = cipher(text, shift , mod)
    print(output)

if __name__ == "__main__":
    main()