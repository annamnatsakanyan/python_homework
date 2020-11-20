print("Calories Calculator")
Gender = input("Enter your gender Male/Female ")
Weight = input("Enter your total weight by Kg ")
Height = input("Specify your height by Cm ")
Age = input("Enter your age by year ")
print("1-Most of the time you spend sitting down, and in your free time you like to walk ")
print("2-Most of the day you spend sitting, and train at least 1 hour a day ")
print("3-During the day you do light physical labor, as well as intensive trenchers at least half an hour, "
      "3-4 times a week ")
print("4-Train at least 1 hour 5-7 times a week, or your work requires a lot of physical activity ")
print("5-An Athlete with non-intensive training, or have a very hard job ")
version = input("Enter yor version ")
if Gender == "Female":
    Calories = 655 + 9.56 * int(Weight) + 1.85 * int(Height) - 4.67 * int(Age)

elif Gender == "Male":
    Calories = 66.5 + 13.75 * int(Weight) + 5 * int(Height) - 6.75 * int(Age)

if version == 1:
    Calories = int(Calories) * 1.2

elif version == 2:
    Calories = Calories * 1.375

elif version == 3:
    Calories = Calories * 1.55

elif version == 4:
    Calories = Calories * 1.7

elif version == 5:
    Calories = Calories * 1.9

print("You need " + str(Calories) + " calories")
input()

