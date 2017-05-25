"""def hows_the_parrot():
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








