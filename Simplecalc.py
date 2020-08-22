import pyttsx3
pyttsx3.speak('A simple Calculator')
print('Simple calculator')
print ('-----------------\n')

print('Select your choice:')
pyttsx3.speak('Select your choice')

pyttsx3.speak(' Hit 1 for Add')
print('\n Hit 1 for Add\n Hit 2 for Subtract\n Hit 3 for Multiply \n Hit 4 for Divide')
pyttsx3.speak('2 for  Subtract')
pyttsx3.speak('3 for Multiply')
pyttsx3.speak('4 for Divide')
ch=input()


n=int(input('Enter the first number'))
m=int(input('Enter the second number'))

if int(ch)==1:
  	d=n+m
elif int(ch)==2:
	d=n-m
	
elif int(ch)==3:
	d=n*m
	
elif int(ch)==4:
	d=n/m
	
print('Result is')
print(d)
pyttsx3.speak('The Result is')
pyttsx3.speak(d)
print('Thank You')
pyttsx3.speak('Thank You')



