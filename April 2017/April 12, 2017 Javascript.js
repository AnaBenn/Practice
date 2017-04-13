/*April 12, 2017 Javascript*/

/*Make Them Bark:

You have been hired by a dogbreeder to write a program to keep record of his dogs.

You've already made a constructor Dog, so no one has to hardcode every puppy.

The work seems to be done. It's high time to collect the payment.

..hold on! The dogbreeder says he wont pay you, until he can make every dog object .bark(). Even the ones already done with your constructor. "Every dog barks" he says. He also refuses to rewrite them, lazy as he is.

You can't even count how much objects that bastard client of yours already made. He has a lot of dogs, and none of them can .bark().

Can you solve this problem, or will you let this client outsmart you for good?

Practical info:

The .bark() method of a dog should return the string 'Woof!'.
The contructor you made (it is preloaded) looks like this:
function Dog(name, breed, sex, age){
    this.name  = name;
    this.breed = breed;
    this.sex   = sex;
    this.age   = age;
}*/

function Dog(name, breed, sex, age){
	this.name = name;
	this.breed = breed;
	this.sex = sex;
	this.age = age;
}

Dog.prototype.bark = function(){
	return ("woof!");
}

Dog.prototype.getInfo = function() {
	return this.name + ', ' + this.breed + ', ' + this.sex + ',' + this.age;
}

var Rufus = new Dog("Rufus", "German Shepard", "Male", 17);


/*Fizz Buzz:

Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value 'Fizz' instead
If the value is a multiple of 5: use the value 'Buzz' instead
If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead*/

function fizzbuzz(x) {
  if(x%3 === 0 && x%5 === 0){
   return "fizz buzz";
  }
  else if(x%3 === 0){
   return "fizz";
  }

  else if(x%5 === 0){
   return "buzz";
  }
  else{
   return x;
 }
}
