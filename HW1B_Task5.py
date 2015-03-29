""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """


""" 
Python code using the functions of dictionary:
items(), keys(), values(), write a program to use all these func-
tions and print the results. """

def main():
  
    data = dict()
    data['school'] = 'Albany'
    data['address'] = '1400 Washington Ave, Albany, NY 12222'
    data['phone'] = '(518) 442-3300'
    
    print data.keys() 
    print data.values()    
    print data.items()
    
if __name__ == '__main__':
    main()