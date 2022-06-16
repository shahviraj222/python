# Declare complex number , find data type, real part, imaginary part, complex conjugate, absolute value of a number
import cmath
import math

x = 3+4j
y = 5j
z = -5j
print(type(x))
print("real number ",x.real)
print("imaginary number ",x.imag)

z=math.sqrt(x.real * x.real + x.imag * x.imag)
c=complex(x.real,-x.imag)
print("Conjugate ",c)
print("print absolute value ",z)
print("Polar ",cmath.polar(z))