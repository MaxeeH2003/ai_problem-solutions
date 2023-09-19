#CAPACITY OF BOTH JUGS
a = int(input("Enter Jug A capacity:"))
b = int(input("Enter Jug B capacity:"))

#INITIAL STATES FOR BOTH JUGS
ai = int(input("Initial water in Jug A:"))
bi = int(input("Initial water in Jug B:"))

#FINAL STATES OF BOTH JUGS
af = int(input("Final state of Jug A:"))
bf = int(input("Final state of Jug B:"))

#PROVIDING OPTIONS
print("1. Fill Jug A completely\n")
print("2. Fill Jug B completely\n")
print("3. Empty Jug A completely\n")
print("4. Empty Jug B completely\n")
print("5. Pour from Jug A till Jug B is filled completely or Jug A becomes empty\n")
print("6. Pour from Jug B till Jug A is filled completely or Jug B becomes empty\n:")
print("7. Pour all from Jug B to Jug A\n")
print("8. Pour all from Jug A to Jug B\n")

#CONDITIONS


while((ai!=af or bi!=bf)):
	if(ai==a and bi==b):
		print("No Solution")
		break
	op = int(input("Enter the operation:"))
	if(op==1):
		ai=a
	elif(op==2):
		bi=b
	elif(op==3):
		ai=0
	elif(op==4):
		bi=0
	elif(op==5):
		if(b-bi>ai):
			bi = ai + bi
			ai=0
		else:

			ai = ai-(b-bi)
			bi=b
	elif(op==6):
		if(a-ai>bi):
			ai=ai+bi
			bi=0
		else:
			bi=bi-(a-ai)
			print("***",ai)
			ai=a
	elif(op==7):
		if(ai<a):
			ai=ai+bi
			bi=0
		else:
			print("Jug A Overflow")
			break
	elif(op==8):
		
		if(bi<b):
			bi=bi+ai
			ai=0
			
		else:
			print("Jug B Overflow")
			break
			
	print(ai,bi)
		
