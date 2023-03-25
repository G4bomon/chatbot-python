import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    even= n%2==0 
    odd= n%2==1

    if odd:
        print ("Weird")
    
    if 2<= n <= 5 and even :
        print("Not Weird")

    if 6<= n <= 20 and even:
        print("Weird")
    
    if 20 < n <=100 and even:
        print("Not Weird")
    
    if 100 < n:
        print ("a") 