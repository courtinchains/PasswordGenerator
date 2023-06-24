# strong password == 1 number, 1 special character, 1 upper case, 1 lower case, min 10 characters

import random  # in order to randomise the information given, making it familiar but yet different
import numpy as np  # in order to turn our random list value into an array

welcome = "Generate strong easy to remember passwords FOR FREE!"
print(welcome)
q1 = input("Firstly, what is the name of your pet?")
q2 = input("When is your birthday? [in numerical form]")
q3 = input("How old will you be in 5 years?[in numerical form]")
q4 = input("What is the name of the street you live on?")
q5 = input("Pick a lucky symbol: [!,@,#,$,%,&]")

# conversions for first question's input
q1A = q1.upper()
q1B = list(q1A)
q1C = random.sample(q1B, len(q1B))
q1D = np.array(q1C)
q1Ea = q1D[0]
q1Eb = q1D[1]
q1Ec = q1D[2]

# conversions for second question's input
q2A = q2
q2B = list(q2A)
q2C = random.sample(q2B, len(q2B))
q2D = np.array(q2C)
q2Ea = q2D[0]

# conversions for third question's input
q3A = q3
q3B = list(q3A)
q3C = random.sample(q3B, len(q3B))
q3D = np.array(q3C)
q3Ea = q3D[0]

# conversions for fourth question's input
q4A = q4.lower()
q4B = list(q4A)
q4C = random.sample(q4B, len(q4B))
q4D = np.array(q4C)
q4Ea = q4D[0]
q4Eb = q4D[1]
q4Ec = q4D[2]
q4Ed = q4D[2]

# the final question's chosen special character
q5A = q5

# transforming our array values into strings in order to form them together
initial_str = str(q1Ea) + str(q1Eb) + str(q1Ec) + str(q2Ea) + str(q3Ea) + str(q4Ea) + str(q4Eb) + str(q4Ec) + str(q4Ed) + str(q5A)

# placing them once again in a list in order to shuffle them up
list_str = list(initial_str)
rand_str = random.sample(list_str, len(list_str))

# finally creating the final password by joining our randomised list
final_pass = ''.join(rand_str)
print("Your password has been generated!:" + " " + final_pass)





