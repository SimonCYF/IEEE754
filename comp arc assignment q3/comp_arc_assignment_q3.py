#Cheah Yee Fei 0129972 comp arc task 1 q3

import time
import sys
import math

#change decimal to binary
def decimalToBinary(decimalNumber, store):
	
	bin=""
	if (decimalNumber >1):
		decimalToBinary( decimalNumber // 2, store)
	x =(decimalNumber%2)
	store.append(str(x))
	for i in range(len(store)):
		bin = bin + str(store[i])
	return(bin)


#main function
def main():
	store = []
	storeExponent = []
	decimalDelList = ""
	z = 3
	sign =""
	decimalValFloat = float(input("Enter a Decimal integer value less than 50 : "))
	IEEE = ""
	ans = ""
	eq = ""
	plc = 0
	
	if int(decimalValFloat) >= 50:
		decimalValFloat=float(input("Please enter a Decimal integer value less than 50 : "))
	elif int(decimalValFloat) < 0:
		sign = 1
		print("Decimal value enter ("+str(decimalValFloat)+ ") is a negative number and sign = "+str(sign))	
		decimalVal = math.trunc(decimalValFloat)
		decimalFloatVal = decimalValFloat - decimalVal
		decimalDelList = decimalVal * -1	
		decimalFloatVal *= -1

	else :
		sign = 0
		#decimalDelList = decimalValFloat
		print("Decimal value enter ("+str(decimalValFloat)+ ") is a positive number and sign = "+str(sign))
		decimalVal = math.trunc(decimalValFloat)
		decimalFloatVal = decimalValFloat - decimalVal
		decimalDelList = decimalVal 
	
	
	print(decimalFloatVal)
	#fraction = round(decimalValFloat - decimalVal,2)
	print("\nCalculating Binary of "+str(decimalVal)+":\n")
	print("\nSystem is converting Decimal (" +str(decimalVal)+ ") into Binary\n")
	binaryFromDecimal=decimalToBinary(decimalDelList, store)
	lengthDecimal = len(binaryFromDecimal)-1
	counterLengthDecimal = len(binaryFromDecimal)-1
	decimalFinalCheck = decimalDelList

	kLK = 0
	while int(decimalDelList)>=2:
		
		plc += 1
		kL99 = decimalFinalCheck % 2
		if lengthDecimal == counterLengthDecimal :
			print("2  |  "+str(decimalFinalCheck)+"       "+str(kL99)+"      = "+str(kL99) +" X 2^" +str(kLK)) 
			print("   |---------")

		t = decimalDelList//2
		decimalDelList = t
		r = decimalDelList % 2		
		lengthDecimal -= 1

		if lengthDecimal > 0 :
			kLK += 1
			print("2  |  "+str(decimalDelList)+"       "+str(r)+"      = "+str(r) +" X 2^" +str(kLK))   
			print("   |---------")

		if lengthDecimal == 0 :
			kLK += 1

			print("      "+str(decimalDelList)+"       "+str(r)+"      = "+str(r) +" X 2^" +str(kLK))

	print("\nDecimal " +str(decimalVal)+" to Binary is " +str(binaryFromDecimal))
	print("Binary " +str(binaryFromDecimal)+" is equal to "+ binaryFromDecimal[0]+"."+binaryFromDecimal[1:]+" * 2^"+str(len(binaryFromDecimal)-1))
	print("The power of the Binary is "+ str(len(binaryFromDecimal)-1))
	
	exponent = 127 + int(len(binaryFromDecimal)-1)
	exponentInBinary = decimalToBinary(exponent,storeExponent)

	print("\nExponent = 127 + "+str(len(binaryFromDecimal)-1))
	lengthDecimalExp = len(exponentInBinary)-1
	counterLengthDecimalExp = len(exponentInBinary)-1
	#exponent = decimalDelList
	stepsShown = 0

	while exponent >=2:
		
		
		exponentVal = exponent % 2
		if lengthDecimalExp == counterLengthDecimalExp :
			print("2  |  "+str(exponent)+"       "+str(exponentVal)+"      = "+str(exponentVal) +" X 2^" +str(stepsShown)) 
			print("   |---------")

		t = exponent//2
		exponent = t
		r = exponent % 2		
		lengthDecimalExp -= 1

		if lengthDecimalExp > 0 :
			stepsShown += 1
			print("2  |  "+str(exponent)+"       "+str(r)+"      = "+str(r) +" X 2^" +str(stepsShown))   
			print("   |---------")

		if lengthDecimalExp == 0 :
			stepsShown += 1

			print("      "+str(decimalDelList)+"       "+str(r)+"      = "+str(r) +" X 2^" +str(stepsShown))

	print("\nExponent " + str(exponent) + " in Binary is " +str(exponentInBinary))
	


	print("\nFormat for IEEE-754")
	print("=========================================================")
	print("| Sign  |  |   Exponent   | |          Mantissa         |")
	print("=========================================================")
	print("| 1 bit |  |     8 bit    | |           23 bit          |")
	print("|   X   |  |   XXXXXXXX   | |  XXXXXXXXXXXXXXXXXXXXXXX  |")
	print("=========================================================")

	
	print("\nSystem is converting to Mantissa and IEEE-754")
	for i in range(1) :
		for e in range(10):
			print(".",end = '  ')		
		time.sleep(1)
		print("\n")


	storeFloatVal =""
	storeArrayFloatVal =""
	for i in range(23):
		if decimalFloatVal < 1:
			storeFloatVal = 0		
			print("==============================================")
			print("| ",round(decimalFloatVal,2) ," X 2 = ",round( decimalFloatVal * 2,2) )
			decimalFloatVal *= 2
			
		if decimalFloatVal > 1:
			storeFloatVal = 1	
			print("==============================================")
			print("| ",round(decimalFloatVal,2) ," - 1 = ",round(decimalFloatVal - 1,2))
			decimalFloatVal -= 1
			
		storeArrayFloatVal += str(storeFloatVal)
		print("|  Bin = ",storeArrayFloatVal)
	print("==============================================\n\n")
	mantissaArray = binaryFromDecimal + storeArrayFloatVal
	print(binaryFromDecimal," + ", storeArrayFloatVal)
	print("Remove first number and last 3 number")
	mantissa = mantissaArray[1:24]
	
	print(" \nMantissa = " +str(mantissa))
	print("\n=========================================================")
	print("| Sign  |  |   Exponent   | |          Mantissa         |")
	print("=========================================================")
	print("| 1 bit |  |     8 bit    | |           23 bit          |")
	print("|   X   |  |   XXXXXXXX   | |  XXXXXXXXXXXXXXXXXXXXXXX  |")
	print("=========================================================")
	
	IEEE = str(sign)+str(exponentInBinary)+str(mantissa)
	IEEEBitForm = ' '.join(IEEE[x:x + 4] for x in range(0, len(IEEE), 4))
	print("|   " + str(sign)+"   |  |   "+str(exponentInBinary)+"   | |  "+str(mantissa)+"  |")
	print("=========================================================")
	print("\nIEEE-754 = sign + exponent + mantissa ")
	print("IEEE-754 = " + str(sign)+" "+str(exponentInBinary)+" "+str(mantissa))
	print("IEEE-754 = " + str(sign)+str(exponentInBinary)+str(mantissa))
	print("IEEE-754 in bit form = "+str(IEEEBitForm))

	
	return 0
	

if __name__ == "__main__":
   main()
