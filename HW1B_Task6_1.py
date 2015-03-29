""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """


""" 
Used json to store dictionary and then print item, key and values. """


import json
def main():
    data = dict()
    data['school'] = 'Albany'
    data['address'] = '1400 Washington Ave, Albany, NY 12222'
    data['phone'] = '(518) 442-3300'
    open('dictionary.txt', 'w').write(json.dumps(data))    
    data = json.loads(open('dictionary.txt').read())	
    print data.keys()
    for key, value in data.items():
        print key, value	 
    print data.values()     
    print data.items()
    
if __name__ == '__main__':
    main()
