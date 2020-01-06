import unittest 
import requests
import json 
from fractions import Fraction 

number1 = [2,21,5,8]
number2 = [7,11,3,4]

add_main = []
add_test = []
sub_main = []
sub_test = []
mul_main = []
mul_test = []
div_main = []
div_test= []

for i in range(0,len(number1)):
        parameters={"A":Fraction(number1[i]),"B":Fraction(number2[i])}

        test_a = number1[i] + number2[i]
        add_test.append(round(test_a,3))

        test_s = number1[i] - number2[i]
        sub_test.append(round(test_s,3))

        test_m = number1[i] * number2[i]
        mul_test.append(round(test_m,3))

        test_d = number1[i] / number2[i]
        div_test.append(round(test_d,3))

        url_a = 'http://127.0.0.1:5000/add'
        r1 = requests.get(url_a, params=parameters)
        data1 = r1.json()
        add_main.append(round(data1,3))

        url_b = 'http://127.0.0.1:5000/sub'
        r2 = requests.get(url_b, params=parameters)
        data2 = r2.json()
        sub_main.append(round(data2,3))

        url_m = 'http://127.0.0.1:5000/mul'
        r3 = requests.get(url_m, params=parameters)
        data3 = r3.json()
        mul_main.append(round(data3,3))

        url_d = 'http://127.0.0.1:5000/div'
        r4 = requests.get(url_d, params=parameters)
        data4 = r4.json()
        div_main.append(round(data4,3))

        if add_main[i] == add_test[i]:
                print("addition successfull:OK")
        else:
                print("addition failed")
        
        if sub_main[i] == sub_test[i]:
                print("subtraction successfull:OK")
        else:
                print("subtraction failed")

        if mul_main[i] == mul_test[i]:
                print("multiplication successfull:OK")
        else:
                print("multiplication failed")

        if div_main[i] == div_test[i]:
                print("division successfull:OK")
        else:
                print("division failed")
