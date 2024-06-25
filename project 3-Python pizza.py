#varaible for the users name and welcome message
name = str(input("Enter your name:"))
print(f"Welcome {name}, to Python Pizza. please follow the prompt to place your order")

#question to choose the size of pizza the customer requires
size = input("What size pizza do you want to order? (Small, Medium, Large): ").lower()

print("Adding pepperoni will cost you more")
add_pepperoni = input("Do you want pepperoni? (Yes or No): ").lower()

print("adding cheese will also cost you more")
cheese = input("Do you want extra cheese? (Yes or No): ").lower()

# Cost Variables
small_pizza = 4000
medium_pizza = 6000
large_pizza = 8000
small_pepperoni = 2000
lm_pepperoni = 3000
extra_cheese = 1000

# Bill Calculation
bill = 0

# Check the size of the pizza
if size == "Small":
    bill += small_pizza
    if add_pepperoni == "Yes":
        bill += small_pepperoni
elif size == "Medium":
    bill += medium_pizza
    if add_pepperoni == "Yes":
        bill += lm_pepperoni
elif size == "Large":
    bill += large_pizza
    if add_pepperoni == "Yes":
        bill += lm_pepperoni

# Check if extra cheese is added
if cheese == "Yes":
    bill += extra_cheese

# Print the final bill and closing remarks
print(f" Thank you for coming to Pyhton Pizza, your final bill is: ₦{bill}")
