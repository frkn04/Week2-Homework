x= str(input("Write a sentence."))
#I want a sentence to be entered here.
#Finally, the program will find how many letters are in the sentence.

letters= { "a": {x.count("a")},
"b": {x.count("b")},
"c": {x.count("c")},
"d": {x.count("d")},
"e": {x.count("e")},
"f": {x.count("f")},
"g": {x.count("g")},
"h": {x.count("h")},
"i": {x.count("i")},
"j": {x.count("j")},
"k": {x.count("k")},
"l": {x.count("l")},
"m": {x.count("m")},
"n": {x.count("n")},
"o": {x.count("o")},
"p": {x.count("p")},
"r": {x.count("r")},
"s": {x.count("s")},
"t": {x.count("t")},
"u": {x.count("u")},
"v": {x.count("v")},
"x": {x.count("x")},
"y": {x.count("y")},
"z": {x.count("z")},
}

my_list=[]
#I created an empty list because it looks like a list in the example.

for a,y in letters.items(): 
    
    if a in x :
       my_list.extend([a,(y)])
    #In the example, letters that are not in the sentence do not appear. So I did it to disable them.

print(my_list)