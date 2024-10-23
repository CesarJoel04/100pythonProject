# print("My age: " + str(12))
# print(123 + 456)

#print(3 * 3 + 3 / 3 - 3)
#print(3 + 3 - 3 / 3 * 3)


# height = 1.65
# weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
# bmi = weight / height**2
# print(bmi)
#
# print(int(bmi))
#
# print(round(bmi))
#
# print(round(bmi, 2))

# score = 0
#
# #User scores a point
# score +=1
# print(score)
#
# #f-strings
# print("Your score is " + str(score))

# score = 0
# height = 1.8
# is_winning = True
#
# print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
