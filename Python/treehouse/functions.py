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



def even_odd(number):
  if number % 2 == 0 :
    return True
  else:
    return False



def squared(item):
    try:
        int(item)
    except:
        return item * len(item)
    else:
        return int(item) ** 2

def fib_intervall(x):
    #returns the largest fibonacci
    number smaller than x and the lowest
    fibonacci number higher than x#
    if x < 0:
        return -1
    (old,new, lub) = (0,1,0)
    while True:
        if new < x:
            lub = new 
            (old,new) = (new,old+new)
        else:
            return (lub, new)
            
while True:
    x = int(input("Your number: "))
    if x <= 0:
        break
    (lub, sup) = fib_intervall(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))

#Elif example

name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

#Elif example 2

name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')

#These statements are similar—both if and while check the value of spam, 
#and if it’s less than five, they print a message. But when you run 
#these two code snippets, something very different happens for each one. 
#For the if statement, the output is simply "Hello, world.". 

#If Statement

spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

#while statement - keep incremeting by one and going back to check if
#spam is less than 5. Once it's greater than 5, it stops printing.

#The code with the if statement checks the condition, and it prints 
#Hello, world. only once if that condition is true. The code with the 
#while loop, on the other hand, will print it five times. It stops 
#after five prints because the integer in spam is incremented by one 
#at the end of each loop iteration, which means that the loop will 
#execute five times before spam < 5 is False.

#In the while loop, the condition is always checked at the start of 
#each iteration (that is, each time the loop is executed). If the 
#condition is True, then the clause is executed, and afterward, 
#the condition is checked again. The first time the condition is 
#found to be False, the while clause is skipped.



spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1


