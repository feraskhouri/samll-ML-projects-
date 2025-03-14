import numpy as np
##class for soft max
class Softmax:
    def numerator(self, x):
        result = np.exp(x)  
        return result

    def denominator(self, x):
        return np.exp(x).sum()  

    def prob(self, x):
        return self.numerator(x) / self.denominator(x)  
#promt the user to enter the number of elements
n = int(input("Enter the number of elements: "))
user_input = []
for i in range(n):
    value = float(input(f"Enter element {i+1}: "))  
    user_input.append(value)  
user_input = np.array(user_input)
softmax_instance = Softmax()
print("Numerator (exp(x)):", softmax_instance.numerator(user_input))
print("Denominator (sum of exp(x)):", softmax_instance.denominator(user_input))
print("Softmax probabilities:", softmax_instance.prob(user_input))
