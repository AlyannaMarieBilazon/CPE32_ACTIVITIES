#ALYANNA MARIE N. BILAZON
#CS3C

#Number functions
#'abs(a)'
print(abs(-10)) 
print(abs(17.5)) 

#'pow(a, b)'
print(pow(2, 4)) 
print(pow(20, 2)) 

#'int(a)'
print(int(5.9)) 
print(int(-5.9))



#Power and Logarithmic functions
import math

# Example: Exponential function
x = 2
exponential_result = math.exp(x)
print("e raised to the power of", x, "is", exponential_result)

# Example: Logarithmic function
num = 100
logarithm_base_10 = math.log10(num)
print("Logarithm (base 10) of", num, "is", logarithm_base_10)



#Trigonometric functions
import math

# Convert degrees to radians
angle_degrees = 20
angle_radians = math.radians(angle_degrees)

# Trigonometric functions
print("Sine:", math.sin(angle_radians))
print("Cosine:", math.cos(angle_radians))
print("Tangent:", math.tan(angle_radians))



#Angular conversion functions
import math

#Convert degrees to radians
angle_in_degrees = 80
angle_in_radians = math.radians(angle_in_degrees)
print("degrees in radians is: ", angle_in_radians)

#Convert radians to degrees
angle_in_degrees = math.degrees(angle_in_radians)
print("radians in degrees is: ", angle_in_degrees)



#Hyperbolic functions
import math

x = 2

# Hyperbolic functions
print("sinh(x):", math.sinh(x))
print("cosh(x):", math.cosh(x))
print("tanh(x):", math.tanh(x))
print("asinh(x):", math.asinh(x))
print("acosh(x):", math.acosh(x))