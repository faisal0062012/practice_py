# A function is a block of code which only run when it is called
# you can pass data, known as parameter, into a function
# Function can return data as a result
# in python, a function is define using def keyword


# lets define a function
def great_user():
    print("Hello, user!")
# great_user()

#example_1
def meet_anyone():
    print("o yaar hore suna ke haal ne tere")
meet_anyone

def aoa():
    print("Assalam o alaikum, All the way from london")
# aoa()
# exp_2
def aoa():
    print("Assalam o alaikum, All the way from shergarh")
# aoa()

def aoa(name):
    print(f"Assalam o alaikum, {name}!, kaifa haluk")
# aoa('')
#exp_3
def slam(name):
    print(f"salamun alika ya habibi, {name}, man anta")
slam('')

def aoa(name= "khuda ke bande"):
    print(f"Assalam o alaikum, {name}!, kaifa haluk")
# aoa('faisal')
#exp_4
def wo_sehre_muhabbat(name= "madina"):
    print(f"sitarun se ye chand kehta hai hr dm,{name}, jesi koi dosri jaga nahen")
wo_sehre_muhabbat



def aoa(name= "khuda ke bande"):
    print(f"Assalam o alaikum, {name}!, kaifa haluk")
# aoa("faisal")


# # Return value

def square(number):
    return number * number
# print(square(9))

# # Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
# print(factorial(3))

# # lambda function

x = lambda a: a + 10
# print(x(5))

x = lambda a, b: a*b
print(x(2, 8))


# ap ne 10 function define krne hen def k sath or lamda k sath