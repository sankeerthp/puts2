import unittest 
import requests
import json 
from fractions import Fraction 

number1 = [23,5,7,13]
number2 = [4,51,33,24]

mul_main = []
mul_test = []

for i in range(0,len(number1)):
        parameters={"A":Fraction(number1[i]),"B":Fraction(number2[i])}

        test_m = number1[i] * number2[i]
        mul_test.append(round(test_m,3))

        url_m = 'http://127.0.0.1:5000/mul'
        r3 = requests.get(url_m, params=parameters)
        data3 = r3.json()
        mul_main.append(round(data3,3))

        if mul_main[i] == mul_test[i]:
                print("multiplication successfull:OK")
        else:
                print("multiplication failed")
