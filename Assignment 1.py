      #Marfo Princess Serwaa
      #Index Number = 2882120
#Question a
w = 10   #load intensity of beam 
Load_intensity = w

L = 12   #length of beam
beam_length = L

x = 0    #Represents a distance on the beam


#M represents the Bending Moment of the beam
M = (w * (-6*x**2 + 6*L*x - L**2))/12

#V represents the Shear Force of the beam
V = w * ((L/2) - x)

print(f'a) Bending Moment when x = 0 is M = {M}KN/m') 
print() #Puts a space between answers in console
print(f'Shear Force when x = 0 is V = {V}KN')

x = 12 #when computing for the Bending moment at the end of the beam, x = L
M = (w * (-6*x**2 + 6*L*x - L**2))/12 # Bending Moment Equation
print()
print(f'Bending Moment when x = 12 is {M}KN/m')

V = w * ((L/2) - x) #Shear Force Equation
print()
print(f'Shear Force when x = 12 is {V}KN')

#Question b
a = -6
b = 72
c = -144

complete_square = b/(2*a)
#Represents the coefficient of x in the quadratic of the form ax^2 + bx + c = 0 of which we multiply by 1/2

constant = -c/a + complete_square**2
#Square the term b/2a and add it to the constant -c/a 
#The constant is - in order to represent the quadratic -6x^2 + 72x - 144 in the form x^2 + bx/a = -c/a 

point_of_contraflexure_1 = (constant**0.5 - complete_square)
point_of_contraflexure_2 = (-constant**0.5 - complete_square)
#point_of_contraflexure_1 and point_of_contraflexure_2 are roots of the quadratic equation.
print()
print(f'b)The distances at which the bending moment will be zero are x1 = {point_of_contraflexure_1} and x2= {point_of_contraflexure_2}') 

#Question c
V = 0 #To find x, Equate V to zero
x = V + (L/2)  
point_of_zero_shear_force = x 
print()
print('c) ' + str(point_of_zero_shear_force) + ' is the point at which the Shear Force is = 0')

#Question d
import numpy as np
beam_length = 12  #Length of the beam in mm(Steps is in mm so convert beam_length to mm)
steps = 0.01 #(mm), convert a step of 10mm to m because the beam_length is in m
w = 10
beam_span = np.arange (0, beam_length + steps, steps) 
x = beam_span #The beam_span is every point on the beam starting from 0 and ending at 12m
M = w * (-6*x**2 + 6*L*x - L**2)/12 #Moment Equation
print()
print('e) The Moment for each step along the span is {0}'.format(M))
#This is to provide the Bending Moment for each value of x within the beam_span



#Question e
start = 0 
step = 0.01 #(mm), convert a step of 10mm to m
k = L + step #L=12m which is the span of the beam
x = np.arange(start,k,step)
V = w*(L/2 - x) #V is the shear force
print()
print('(e) The shear force for each step along the span is {}'.format(V))
#This is to provide the shear force(V) for each value of x within the beam_span

#Question f
"""
Let the absolute value of the bending moment array be AM
Also let the minimum AM be m_AM
"""
AM = abs(beam_span) #Find the values of x within the beam_span that are close to zero and take them to zero
m_AM = min(AM) #This operation is carried out because Bending Moment is minimum when x = 0(Absolute)
"""
When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
"""

#from the above expression
a = 1
b = -L
c = (L**2/6)+(2*m_AM)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print()
print(f'f)The points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))     


#Question g
"""
Let the relative errors be r_error
"""
r_error_1 = ((9.464101615137753-9.46)/9.464101615137753*100)
r_error_2 = (( 2.539999999999999-2.5358983848622456)/2.539999999999999*100)
print()
print('(g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r_error_1,r_error_2))



#Question h
import numpy as np
def calculate_M(w, L, x):
    return(w * (-6*x**2 + 6*L*x - L**2)/12) 

beam_length = 12
steps = 10
Moment_values = [] #An empty list to store moment values for each value of x in beam_span

for x in beam_span:
    M = calculate_M(w, L, x)
    Moment_values.append(M) #Fill the empty list created above with the moment values obtained
    
max_BM = max(Moment_values) 
min_BM = min(Moment_values) 

print()
print("h) Maximum bending moment:", max_BM) #Print max bending moment


print()
print("Minimum bending moment:", min_BM) #Print minimum bending moment

#Github username = PrincessAB
print()
print('#Github username = PrincessAB')
    
    
    

    
   
   
    
    
    
    
  
   
    
    
    
   
    
   
    
   




    
    
    


