import numpy as np
import matplotlib.pyplot as plt

R1=12
R2=3
V=12

A =np.array([[1,1],
             [12,3]
])
print(A)
B = np. array([3,V])
I =np.linalg.solve(A, B)
I1= I[0]
I2= I[1]
print ("Current through R1 :", round (I1, 2) ,"A")
print ("Current through R2 :", round (I2, 2) , "A")

V1= I1*R1
V2= I2*R2

print ("Voltage through R1 :", round (V1, 2), "V")
print ("Voltage through R2 :", round (V2, 2), "V")

print("currents:",I)
components = ["R1","R2"]
voltages =[V1,V2]
plt.bar(components,voltages)
plt.title("Voltage drop accross all component")
plt.xlabel("components")
plt.ylabel("Volage (V)")
plt.show()
