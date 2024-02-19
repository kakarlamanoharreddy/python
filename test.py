#Practice
#from sys import *
# script, Manohar, Reddy, Kakarla = argv
# print('The script is called',script)
# print('The first name is called',Manohar)
# print('The second name is called',Reddy)
# print('The Third name is called',Kakarla)

#Command line arguments
# from sys import argv
# from sys import *
# print(argv[0])
# print(argv[1])
# print(argv[2])
# print(type(argv))

#program to print sum of given numbers provided as command line arguments
# from sys import *
# args=argv[1:]
# sum=0
# for x in args:
#     sum = sum + int(x)
# print('The sum is:',sum)


#Program to print command line arguments information
# from sys import *
# print('The no.of command line arguments:',len(argv))
# print("\n")
# print('The list of command line arguments:',argv)
# print("\n")
# print('Command line arguments one by one:\n')
# for x in argv:
#     print(x)
    
from sys import argv
print(argv[1])
print(argv[1]+argv[2])
print(int(argv[1])+int(argv[2]))

