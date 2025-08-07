import random

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

def password_generator(total_len, nr_letters, nr_numbers, nr_symbols):
    pass_list = []
    for i in range(nr_letters):
        pass_list.append(random.choice(letters))
    for j in range(nr_numbers):
        pass_list.append(random.choice(numbers))
    for k in range(nr_symbols):
        pass_list.append(random.choice(symbols))
    
    # Filling the empty spaces if needed rabdomly
    remaining = total_len - (nr_letters + nr_numbers + nr_symbols)
    if remaining > 0:
        all_chars = letters + numbers + symbols
        for l in range(remaining):
            pass_list.append(random.choice(all_chars))

    random.shuffle(pass_list)
    return ''.join(pass_list)

# Main Programme
def main():
    while True:
        try:
            total_len = int(input("Enter total password length: "))
            nr_letters = int(input("Enter number of letters: "))
            nr_symbols = int(input("Enter number of symbols: "))
            nr_numbers = int(input("Enter number of numbers: "))

            if total_len < (nr_letters + nr_symbols + nr_numbers):
                print("Total length must be atleast equal to sum of letters, symbols and numbers")     
            else:
                break
        except ValueError:
            print("Please enter valid numbers only. \n")
    password = password_generator(total_len, nr_letters, nr_numbers , nr_symbols)
    print(f"Generated Password: {password}")    

if __name__ == "__main__":
    main()