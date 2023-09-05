#introduction
sent1 = "my name is Mahamadou"
age = "i am 21 years old"
sent2 = " and I like to play basketball."
sent3 = "so what i am doing right now is getting familiar with python and the IDE."
combine_sentence = sent1 + "," + age + "," + sent2 + sent3
print(combine_sentence)

#adding
print(10 + 15)

#Multiplying
print(47837 * 848494949)

#Dividing
print(90/10)

#Salary
salary = 40 * 52
wage = 40
print(salary * wage)


#Age Checker
age = 21
if age < 13:
    print("you are not yet a teenager")
elif age < 18:
    print("you are a teenager")
else:
    print("you are an adult")


#Percentage Calculator
percentage = (52/80)
formatted_percentage = "{:.2%}".format(percentage)
print(formatted_percentage)
