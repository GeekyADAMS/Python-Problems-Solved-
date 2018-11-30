#! Python3
"""
Fibonacci Sequence solutions written by Geeky Adams.

  This is a program to solve a Fibonacci sequence problem according to the length of sequence needed by the user.
A Fibonacci sequence is a sequence of new numbers formed when the last two number of a sequence add up to form new ones.

For example:
  [0,1,1,2,3,5,8,13,21] is a Fibonacci sequence because each new number of the sequence is formed by the addition of the previous two numbers.
  0+1 = 1, 1+1 = 2, 1+2 = 3, 2+3 = 5 and so on...
"""

# The below collects an input of the number or length of Fibonacci sequence desired to be printed by user.
# It then converts it to an integer for the sake of operations...
nth_term = int(input("Enter length of Fibonacci sequence to be printed: "))

# Here we declare our first two Fibonacci numbers which are usually 0 and 1 by default unless altered.
firstNumber = 0
secondNumber = 1

# Below we create a list to store our Fibonacci Sequence and we call our Fibonacci list fiboList.
fiboList = []

# Next below we store our predefined First and Second Fibonacci Numbers in the fiboList by concatenation.
# Concatenation in list means adding two or more lists together. Here, We concatenated fiboList with some new undefined list.

fiboList= fiboList + [firstNumber]
fiboList= fiboList + [secondNumber]

# i below depicts a counter. We need a counter to keep track of the iteration so as to regulate the number of Fibonacci numbers printed.
i = 0

# The below block of code handles the iteration.

while i < nth_term - 2 :          #If i is less than user defined length minus 2, it repeats. If else it stops.
                                  #We need to do the above to avoid endless iteration which would use up the whole computer memory.
                                  #It is nth_term minus 2 because we already have 2 predefined fibonacci numbers which are the first number and the second.

    z = firstNumber+secondNumber  # Here we add the first two numbers together to get a new Fibonacci number z.
    fiboList = fiboList + [z]     #Here we added the new Fibonacci number (z) to the Fibonacci list.

    firstNumber = secondNumber    #Now to proceed with the sequence, we need to make first number the second number and
    secondNumber = z              # the second number the new z.
    i+=1                          # We make an increment to the counter i so as to keep track of the number of Fibonacci numbers added to the list already.

# we have escaped the iteration block, now lets print out our Fibonacci list.
print(fiboList)

