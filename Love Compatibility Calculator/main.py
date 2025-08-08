def love_compatibility_calculator(name1 , name2):
    check1 = ["T", "R", "U", "E"]
    check2 = ["L", "O", "V", "E"]

    lst = list((name1 + name2).replace(" ", "").upper())

    t_times = 0
    l_times = 0

    for i in lst:
        if i in check1:
            t_times += 1         

    for j in lst:
        if j in check2:
            l_times += 1

    love_comp_per = int(str(t_times) + str(l_times))

    if love_comp_per > 70:
        print(f"Your love compatibility is {love_comp_per}")
        print("You form an ideal couple")
    elif love_comp_per > 50:
        print(f"Your love compatibility is {love_comp_per}")
        print("Your love compatibility is decent")
    elif love_comp_per > 25:
        print(f"Your love compatibility is {love_comp_per}")        
        print("Low Score tbh.")    
    else:
        print(f"Your love compatibility is {love_comp_per}")        
        print("Low Score don't think are much compatible with each other")    

def main():
    print("Hey There! Let's check your love compatibility score")
    print("Enter your's and your partner's name here and we will get back to you with a compatibility score. ")

    while True:
        n1 = input("Enter your name here: ")
        n2 = input("Enter your partner's name here: ")
        love_compatibility_calculator(n1, n2)

        again = input("Do you want to check another couple? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for using the love compatibility calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
