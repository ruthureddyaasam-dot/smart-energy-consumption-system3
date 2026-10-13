import analysis
print("SMART ENERGY CONSUMPTION SYSTEM")
print("--------------------------------")

print("1. View Energy Analysis")
print("2. Predict Future Consumption")
print("3. Energy Saving Suggestions")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
   import analysis

elif choice == "2":
 import  prediction

elif choice == "3":
    print("import Energy Saving Suggestions.")

elif choice == "4":
    print("Thank you for using the system!")

else:
    print("Invalid choice. Please try again.")