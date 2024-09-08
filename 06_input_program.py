# name = input("Enter your name:") 
# print("Hello", name, ", or sunao")

# if __name__ == '__main__':
#    name = input("Enter your name: ")
#    print("Hello", name, "or sunao")

# name = input("person a what is your name")
# print("Hello", name)

# name = input("person b what is your name")
# print("Hello", name)

# name = input("person a what is your age")
# print("my age is", name)

# name = input("person b what is your age")
# print("my age is", name)

# Taking input for the first person
# name1 = input("Enter the name of the first person: ")
# age1 = float(input("Enter the age of the first person: "))

# # Taking input for the second person
# name2 = input("Enter the name of the second person: ")
# age2 = float(input("Enter the age of the second person: "))

# # Comparing ages
# if age1 > age2:
#     print(f"{name1} is older than {name2}.")
# elif age1 < age2:
#     print(f"{name2} is older than {name1}.")
# else:
#     print("Both persons are of the same age.")

# BMI of person

person_A_name = input("what is your name:")
person_A_height = input("what is your height in meters?")
person_A_weight = input("what is your weight in kgs?")

person_B_name = input("what is your name:") 
person_B_height = input("what is your height in meters?")
person_B_weight = input("what is your weight in kgs?")

# bmi = weight / (height ** 2)

BMI_person_A = float(float(person_A_weight)/float(person_A_height))
BMI_person_B = float(float(person_B_weight)/float(person_B_height))

print("BMI of person A is", BMI_person_A)
print("BMI of person B is", BMI_person_B)

if BMI_person_A>BMI_person_B:
    print(person_A_name, "is healthier than", person_B_name)
else:
    print(person_B_name, "is healthier than", person_A_name)
