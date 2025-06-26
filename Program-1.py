class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def Function(self,Calculate):
        if Calculate=='+' or  Calculate=='add':
            return self.a + self.b
        elif Calculate=='-' or Calculate=='sub':
            return self.a-self.b
        elif Calculate=='*' or Calculate=='multiply':
            return self.a*self.b
        elif Calculate=='/' or Calculate=='division':
            if self.a==0 or self.b==0:
                return 'Error Because Division By 0'
            else:
                return self.a/self.b
        else:
            return 'Invalid Operation,Please enter valid from this (+,-,*,/) or (add,sub,multiply,division)'

a=float(input('Enter the value : '))
b=float(input('Enter the value : '))
Calculate=input('Enter the Operation like a (+,-,*,/) or (add,sub,multiply,division): ').lower()
c=Calculator(a,b)
result=c.Function(Calculate)

print('result is :', result )


