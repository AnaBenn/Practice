def hows_the_parrot():
	print("He's pining for the fjords!")

hows_the_parrot()



def lumberjack(name):
	if name.lower() == 'anastasia':
		print("Anastasia's a lumberjack and she's OK")
	else:
		print("{} sleeps all night and {} works all day!".format(name, name)) 

lumberjack("Turkey")



def lumberjack(name, pronoun):
		print("{}'s a lumberjack and {}'s OK".format(name, pronoun))

lumberjack("Pineapple", "she" )
lumberjack("Shrimply Pibbles", "he" )
lumberjack("Joseph", "they're" )



def average(num1, num2):
	return (num1 + num2) / 2

avg = average(2, 8)
print(avg)



def printer(count):
    greetings = count * "Hi "
    print(greetings)

printer(10)



def product(num1, num2):
    return num1 * num2

result = product(5, 63)
print(result)









