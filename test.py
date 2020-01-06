import unittest 
import requests
import json 
from fractions import Fraction 

number1 = [2,21,5,8]
number2 = [7,11,3,4]

sub_main = []
sub_test = []

for i in range(0,len(number1)):
        parameters={"A":Fraction(number1[i]),"B":Fraction(number2[i])}

        test_s = number1[i] - number2[i]
        sub_test.append(round(test_s,3))

        url_b = 'http://127.0.0.1:5000/sub'
        r2 = requests.get(url_b, params=parameters)
        data2 = r2.json()
        sub_main.append(round(data2,3))
        
        if sub_main[i] == sub_test[i]:
                print("subtraction successfull:OK")
        else:
                print("subtraction failed")
