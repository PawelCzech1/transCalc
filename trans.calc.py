# kalkulat or cen t�umacze�
# napisa� program,zliczaj�cy znaki
print("Program dla tłumaczy")
print("Wylicz koszt tłumaczenia")
print("##########")

pricePl = 31.5
priceHu = 33.75

language = input("Enter the translation language:\t ")
character = int(input('Enter the character amount  of the document\t'))
if language == "polski" or 'pl':
    print("You choosen the translation for pl language")
    
   
    pages = character / 1800.0
    print(f"pages amount\t {round(pages,2)}" )

else:
    print("Hungarian translation")

    pages = character / 1800.0
    print(f"pages amount\t {round(pages,2)}" )

def getPrice(): 
    if(language == "pl" or language == "polski"): 
        totalPrice = pages * pricePl
        print(f"You have to pay {round(totalPrice,2)}.\nThank you for your cooperation")
    else: 
         totalPrice = pages * priceHu
         print(f"You have to pay {round(totalPrice,2)}.\nThank you for your cooperation")

getPrice()




    

