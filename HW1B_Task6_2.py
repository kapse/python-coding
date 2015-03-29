""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """


""" This task is about how to store a number of different types
objects (e.g., list, dictionary, array) to a le and then load the
objects from the le. """

import json
def main():
    a = [1, 2, 3, 4, 5]
    data = dict()
    data['school'] = 'Albany'
    data['address'] = '1400 Washington Ave, Albany, NY 12222'
    data['phone'] = '(518) 442-3300'
	
    file = open('data1.txt', 'w')
    file.write(json.dumps(a) + '\n')
    file.write(json.dumps(data) + '\n')
    file.close()
    a = open('data1.txt').readlines()
    array = json.loads(a[0])
    dictionary= json.loads(a[1])
    print 'Array: ', array
    print 'Dictionary: ',dictionary
    
if __name__ == '__main__':
    main()