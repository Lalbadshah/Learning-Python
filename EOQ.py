import math

D=int(raw_input("Enter Demand: "))
S=int(raw_input("Enter Setup Cost: "))
H=float(raw_input("Holding Cost: "))

EOQ = math.floor(math.sqrt(2*D*S/H))
print("EOQ ="+str(EOQ))
Q=int(raw_input("Enter Value for Q (Order quantity) to find prices:"))
AHC=Q*H/2
ASC=D*S/Q
print("Annual Holding cost = "+str(AHC))
print("Annual Setup cost = "+str(ASC))
