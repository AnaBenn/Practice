try:
	count = int(input("Give me a number: "))
except ValueError:
	print ("That's not a number silly!")
else:
	print("Hi " * count)


def add(num1, num2):
    try:
        return float(num1) + float(num2)
    except ValueError:
        return None
    else:
        print(num1 + num2)

sum = add(12, 13)

print (sum)
