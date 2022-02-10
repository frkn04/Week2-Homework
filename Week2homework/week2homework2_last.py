import collections


number = int(input("How many elements would you like to create a list of numbers?"))
#I requested input from the user to determine the number of elements of the list.

number_list= []
#I created an empty list.

for i in range(1,number+1):
     number_list.append(i)
#I added as many elements as the number specified by the user to the list I created.

print(number_list)
#I showed the created list..

slide = int(input("Write how many numbers you want to shift?"))
#I asked the user how many numbers the element would like to shift?
#If the user wants to slide backwards, he/she must add minus beforethe number when entering.

number_list = collections.deque(number_list)
number_list.rotate(slide)
#I added the formula that ı saw on the internet.

print(number_list)



