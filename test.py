import unittest 
import requests
import json 
from fractions import Fraction 

number1 = [23,5,7,13]
number2 = [4,51,33,24]

add_main = []
add_test = []

for i in range(0,len(number1)):
        parameters={"A":Fraction(number1[i]),"B":Fraction(number2[i])}

        test_a = number1[i] + number2[i]
        add_test.append(round(test_a,3))

        url_a = 'http://127.0.0.1:5000/add'
        r1 = requests.get(url_a, params=parameters)
        data1 = r1.json()
        add_main.append(round(data1,3))


        if add_main[i] == add_test[i]:
                print("addition successfull:OK")
        else:
                print("addition failed")
