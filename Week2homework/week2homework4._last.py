x = str(input("Please write a word."))
y= str (input("Please write another word."))
#I asked the user to enter two words.

x = x.lower()
y = y.lower()
#Since the question asked for lowercase letters, I changed the input to lowercase.

my_set1 = set(x)
my_set2 = set(y)
#I converted the values that were str before to set.

instersection= my_set1.intersection(my_set2)
diffrence1 = my_set1.difference(my_set2)
diffrence2= my_set2.difference(my_set1)
#I have defined the here intersection and their difference

sort_intersection = list(instersection)
sort_intersection.sort()
sort_diffrence1=list(diffrence1)
sort_diffrence2=list(diffrence2)
#I converted the values that were previously Set to List.

my_list =[f"{sort_intersection} {sort_diffrence1} {sort_diffrence2}"]

print(my_list)