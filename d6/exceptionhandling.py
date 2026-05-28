#Handle divide-by-zero exception in calculator program
try:
    num1 = 20
    num2 = 0

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


#Handle invalid input exception while taking integer input
try:
    num = int(input("Enter an integer: "))

    print("You entered:", num)

except ValueError:
    print("Error: Please enter a valid integer")

#Handle file not found exception
try:
    f = open("data.txt", "r")

    content = f.read()

    print(content)

    f.close()

except FileNotFoundError:
    print("Error: File not found")

#Handle multiple exceptions in a single program
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ValueError:
    print("Error: Please enter valid integers")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


#Use finally block to close file properly
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#Create custom exception for invalid age input
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter age: "))

    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age!")

    print("Valid age:", age)

except InvalidAgeError as e:
    print("Error:", e)

except ValueError:
    print("Enter valid integer")

#Create custom exception for insufficient bank balance
class InsufficientBalanceError(Exception):
    pass

try:
    balance = 1000
    withdraw = int(input("Enter amount to withdraw: "))

    if withdraw > balance:
        raise InsufficientBalanceError("Not enough balance")

    balance -= withdraw
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print("Error:", e)


#Handle index out of range exception in list operations
try:
    nums = [10, 20, 30]
    print(nums[5])

except IndexError:
    print("Error: Index out of range")


#Handle key error exception in dictionary access
try:
    student = {"name": "Aman", "age": 20}
    print(student["marks"])

except KeyError:
    print("Error: Key not found")



#Handle value error in type conversion
try:
    num = int(input("Enter number: "))
    print(num)

except ValueError:
    print("Error: Invalid number format")


#Create login system with exception handling
try:
    username = "admin"
    password = "1234"

    if username != "admin":
        raise Exception("Invalid username")

    if password != "1234":
        raise Exception("Invalid password")

    print("Login successful")

except Exception as e:
    print("Login failed:", e)


#Raise exception if password is too weak
try:
    password = input("Enter password: ")

    if len(password) < 6:
        raise Exception("Password too weak")

    print("Strong password")

except Exception as e:
    print("Error:", e)


#Build safe file reader using try-except-finally
try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution completed")
    try:
        file.close()
    except:
        pass

#Create ATM system with proper exception handling
try:
    balance = 5000

    amount = int(input("Withdraw amount: "))

    if amount <= 0:
        raise Exception("Invalid amount")

    if amount > balance:
        raise Exception("Insufficient balance")

    balance -= amount
    print("Withdraw successful")
    print("Remaining balance:", balance)

except ValueError:
    print("Enter valid number")

except Exception as e:
    print("Error:", e)

#Implement nested try-except blocks in a real-world program
try:
    try:
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid input inside inner block")
        num = 0

    try:
        result = 10 / num
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero")

except Exception as e:
    print("General error:", e)



