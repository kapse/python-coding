""" 
Name : VAIBHAV KAPSE
Studnt ID : 001201067
Course : CSI531 Data Mining """

""" 
Store a list to a le, which is item= [1, 2, 3, 4, 5], and then load
the list. Print the list nally. Note: save a list into a le by
using json.dumps(). """


import json
def main():
	ele=[1,2,3,4,5]
	open('storeele.txt','w').write(json.dumps(ele))
	read_contents=json.loads(open('storeele.txt').read())
	print read_contents
	
if __name__=='__main__':
	main()