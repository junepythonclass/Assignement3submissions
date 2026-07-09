# Student Registration Program

# Ask the user to enter their information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")
phone_number = input("Enter your phone number: ")
track = input("Enter your track (Python or JavaScript): ").lower()
cohort = input("Enter your cohort: ")

# Check eligibility
if age < 15:
    print("\nSorry,", name + ".", "You are not eligible for any program.")

elif track != "python" and track != "javascript":
    print("\nSorry,", name + ".", "You are not eligible for CSE.")

else:
    print("\n===== STUDENT DETAILS =====")
    print("Name:", name)
    print("Age:", age)
    print("Location:", location)
    print("Phone Number:", phone_number)
    print("Track:", track.title())
    print("Cohort:", cohort)
    print("\nCongratulations! You are eligible for CSE.")