# welcome screen

print("=" * 50)
print("    STUDENT CLUB REGISTRATION SYSTEM")
print("=" * 50)
print()
print("Welcome! Let's get you registered for our club.")
print()

#Personal Information
print("--- Personal Information ---")
print()


member_name = input("Enter your full name: ")


age = int(input("Enter your age: "))

student_id = input("Enter your student ID number: ")

email = input("Enter your email address: ")

phone_number = input("Enter your phone number: ")

print()

#Membership Preferences
print("--- Membership Preferences ---")
print()

membership_duration_years = int(input("How many years would you like to register for? "))

num_activities = int(input("How many club activities would you like to join? "))

discount_card_input = int(input("Do you have a student discount card? (Enter 1 for Yes, 0 for No): "))
has_discount_card = bool(discount_card_input)

print()

#Payement Information
print("--- Registration Fees ---")
print()

base_registration_fee = float(input("Enter the base registration fee (CFA): "))

activity_fee_per_unit = float(input("Enter the cost per activity (CFA): "))

print()
print("Processing your registration...")
print()

#Fee Calculations
current_year = 2025

# Arithmetic Expression 1: Calculate total activity fees
total_activity_fees = num_activities * activity_fee_per_unit

# Arithmetic Expression 2: Calculate subtotal before discount
subtotal_before_discount = base_registration_fee + total_activity_fees

# Arithmetic Expression 3: Calculate discount amount
discount_amount = (subtotal_before_discount * 0.05) * has_discount_card

# Arithmetic Expression 4: Calculate final total
final_total_fee = subtotal_before_discount - discount_amount

# Arithmetic Expression 5: Calculate membership end year
membership_end_year = current_year + membership_duration_years

# Arithmetic Expression 6: Calculate age at membership end
age_at_membership_end = age + membership_duration_years


print("=" * 50)
print("        REGISTRATION SUMMARY")
print("=" * 50)
print()
print("PERSONAL INFORMATION")
print("-" * 50)
print(f"Name: {member_name}")
print(f"Age: {age} years")
print(f"Student ID: {student_id}")
print(f"Email: {email}")
print(f"Phone: {phone_number}")
print()

#Membership Details
print("MEMBERSHIP DETAILS")
print("-" * 50)
print(f"Membership Duration: {membership_duration_years} year(s)")
print(f"Number of Activities: {num_activities}")
print(f"Discount Card Holder: {has_discount_card}")
print(f"Membership Valid Until: {membership_end_year}")
print(f"Your Age at End of Membership: {age_at_membership_end} years")
print()

#Financial Summary
print("FINANCIAL SUMMARY")
print("-" * 50)
print(f"Base Registration Fee: {base_registration_fee:.2f} CFA")
print(f"Activity Fees ({num_activities} x {activity_fee_per_unit:.2f}): {total_activity_fees:.2f} CFA")
print(f"Subtotal: {subtotal_before_discount:.2f} CFA")
print(f"Discount (5%): -{discount_amount:.2f} CFA")
print("-" * 50)
print(f"TOTAL AMOUNT DUE: {final_total_fee:.2f} CFA")
print()

#Confirmation Message
print("=" * 50)
print(f"Thank you, {member_name}!")
print("Your registration has been recorded.")
print("Welcome to our club!")
print("=" * 50)
