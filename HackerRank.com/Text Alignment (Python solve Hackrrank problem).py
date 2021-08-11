'''#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))'''


# function diye korano hoyeche...
number = int(input())

def cone (number):
    width = number
    h = ""
    for i in range(width):
        h = 'H'*(i+1) + "H"*i
        h = h.rjust(width+i,' ') 
        print (h)
    space = ((1 +(2*(number-1))) - number)/2
    return(space)

def alpha_H(number,space):
    for i in range(number+1):
        h = 'H'*number
        line = h.rjust(len(h)+space," ") + h.rjust(len(h) *4," ")
        print(line)
    for i in range((number+1) //2):
        line = (h*5).rjust(len(h)*5 +space, " ")
        print (line)
    for i in range(number+1):
        h = 'H'*number
        line = h.rjust(len(h)+space," ") + h.rjust(len(h) *4," ")    
        print(line)
        
def r_cone (number,space):
    width = (number * 5)
    h = "" 
    for i in range(number,-1,-1):
        h = 'H'*(i-1) + "H"*i
        h = h.rjust(width +i -1 ,' ')
        print (h)
 
        
space = int(cone(number))
alpha_H(number,space)
r_cone(number,space)
