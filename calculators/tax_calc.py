#Make a function that counts how much takes you have to pay per year 

def tax_count(income):
    print("This is based on swedish taxing rules. It's just an esstimate, please double cheack any margins.")
    if income <= 24873: 
        print("You're paying 0% in taxes")
        return 0
    
    if income <= 625800:
        total = income * 0.32
        print("You're paying 32% in taxes")
        return total
    
    else: 
        temp = (income - 625800) * 0.2
        ground_rate = 625800 * 0.32 #taxes the group rate of ca 32%
        total = temp + ground_rate
        return total


total_tax = tax_count(400000)

print(f"You have to pay {total_tax} SEK in taxes")

if total_tax >= 150000: 
    print("Yikes!")
else: 
    print("Good for you!")


