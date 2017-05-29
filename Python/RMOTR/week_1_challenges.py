#if list is greater than 3 it returns True

def more_than_3_elements(a_list):
    if len(a_list) > 3:
        return(True)
    else:
        return(False)

#if variable is a str it returns True

def is_string(variable):
    if type(variable) == str:
        return(True)
    elif type(variable) != str:
        return(False)

#that receives two numbers and returns  the sum of them ONLY if 
#they’re both integers

def add_only_integers(a, b):
    if (type(a) == int and type(b) == int):
        return (a + b)
    else:
        return("invalid parameters")

#receives a number and returns True if it is greater than 10 OR less than 
#0 and False otherwise.

def check_out_of_boundaries(number):
	if number > 10 or number < 0:
		return(True)
	else:
		return(False)

#Define a function traffic_light that receives a color and returns:
#'stop' if the color is red
#'slow down' if the color is yellow
#'go' if the color is green

def traffic_light(color):
	if color == 'red':
		return('stop')
	elif color == 'yellow':
		return('slow down')
	elif color == 'green':
		return('go')

#Define a function color_mixer that receives two colors color1 and color2 
#and returns the color resulting from mixing them in EITHER ORDER. 
#The colors received are either red, blue, or yellow and you should return:

#Magenta if the colors mixed are red and blue

#Green if the colors mixed are blue and yellow

#Orange if the colors mixed are yellow and red

def color_mixer(color1, color2):
	if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
		return('Magenta')
	elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
		return('Green')
	elif (color1 == 'yellow' and color2 == 'red') or (color1 == 'red' and color2 == 'yellow'):
		return('Orange')

#Define a function get_grade_letter that receives a score and you should return:

#'A' if the score is 90 or above

#'B' if the score is 80 to 89

#'C' if the score is 70 to 79

#'D' if the score is 60 to 69

#'F' if the score is less than 60

def get_grade_letter(score):
	if score >= 90:
		return('A')
	elif score >= 80:
		return('B')
	elif score >= 70:
		return('C')
	elif score >= 60:
		return('D')
	elif score < 60:
		return('F')

#Define a function powers_of_two that receives a power and uses a for loop
#to calculate and return 2 to that power. Do not use the math.pow or or the x**y 
#operator for this assignment.


def powers_of_two(power):
	raised = 1
	for _ in range(power):
		raised *= 2
	return raised


#Define a function sum_of_numbers_in_list that receives a list of 
#numbers a_list of an unknown length and calculates the sum of those 
#numbers using a for loop. Do not use the sum function.

def sum_of_numbers_in_list(a_list):
	sum = 0
	for i in a_list:
		sum = sum + i
	return sum
	


    




