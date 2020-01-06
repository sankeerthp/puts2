import unittest 
import requests
import json 
from fractions import Fraction 

number1 = [2,21,5,8]
number2 = [7,11,3,4]

div_main = []
div_test= []

for i in range(0,len(number1)):
        parameters={"A":Fraction(number1[i]),"B":Fraction(number2[i])}

        test_d = number1[i] / number2[i]
        div_test.append(round(test_d,3))

        url_d = 'http://127.0.0.1:5000/div'
        r4 = requests.get(url_d, params=parameters)
        data4 = r4.json()
        div_main.append(round(data4,3))

        if div_main[i] == div_test[i]:
                print("division successfull:OK")
        else:
                print("division failed")
