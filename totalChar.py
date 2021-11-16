character = int(input("Enter the character amount, please:\t"))

def char_count():
    if character != "": 
        print("do you wanna enter the next value? 'y' or 'n'?\t")
        if answer == 'y': 
            character = int(input("Enter the next value. "))
            totalChar = character + character
            print(f'Total amount of the document equal {totalChar}')
        else:
            totalChar = character 
            rint(f'Total amount of the document equal {totalChar}')
        
char_count()
    


