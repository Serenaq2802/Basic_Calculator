print ("\n" + "=" * 60)
print ("                     Basic Calculator ")
print ("=" * 60 + "\n")

# Define Operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    if y == 0:
        return "Error! Division by Zero."
    else:
        return x / y
    
# Format numbers to remove .0 if integer
def format_number(n):
    if isinstance(n, float) and n.is_integer():
        return str(int(n))
    else:
        return str(n)

# Main Loop
while True: 
    print("Select Operation:\n")
    print("1️⃣  → ➕ Add ")
    print("2️⃣  → ➖ Subtract ")
    print("3️⃣  → ✖️  Multiply ")
    print("4️⃣  → ➗ Divide ")
    print("5️⃣  → ❌ Quit\n")
    print("-" * 40)
    print()

    choice = input("\nEnter Selected Operation (1/2/3/4/5): ").strip()

    if choice == '5':
        print ("\nThanks for calculating with us. See you next time!\n")
        break

    if choice in ('1','2','3','4'):
        # Get User Numbers
        num1 = input ("Enter First Number: ").strip()
        num2 = input ("Enter Second Number: ").strip()

        # Validate Numbers
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        # Perform selected operation
        print("\n The result is: ")
        print("-" * 40)

        if choice == '1':
            result = add(num1, num2)
            print(f" {format_number(num1)} + {format_number(num2)} = {format_number(result)}\n")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f" {format_number(num1)} - {format_number(num2)} = {format_number(result)}\n")
        elif choice == '3':
            result = multiply(num1, num2)
            print (f" {format_number(num1)} * {format_number(num2)} = {format_number(result)}\n")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result,str):
               print(f"{result}\n")
            else:
               print (f" {format_number(num1)} / {format_number(num2)} = {format_number(result)}\n")
         
        print ("-" * 40 + "\n")
    else:
        print("Invalid choice. Please select a valid option.\n")