""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """

""" 
Similar to Task 3, but here we consider two lists. Print these
two lists nally. items1 = [1, 2, 3, 4, 5], items2 = [6, 7, 8, 9, 10] """

import json
def main():
    items1 = [1, 2, 3, 4, 5]
    items2 = [6, 7, 8, 9, 10]
    file = open('storeele1.txt', 'w')
    file.write(json.dumps(items1) + '\n')
    file.write(json.dumps(items2) + '\n')
    file.close()
    a = open('storeele1.txt').readlines()
    i1 = json.loads(a[0])
    i2= json.loads(a[1])
    print i1,i2
    
    
if __name__ == '__main__':
    main()