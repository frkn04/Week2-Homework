my_list = []
#I created an empty list here
for x in range(1,23):
    my_list.append(x)
#I added the numbers from 1 to 22 with the for loop in the list.
print(my_list)
#This way I got the first output requested in the question.
del my_list[1::2]
print(my_list)
#Since it then asked us to remove every second element, I defined it starting from 1 and deleted the numbers by skipping 2 each.
del my_list[2::3]
#In the same way I continued to describe
print(my_list)
del my_list[3::4]
print(my_list)
del my_list[4::5]
print(my_list)