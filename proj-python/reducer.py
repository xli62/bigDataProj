#!/usr/bin/python
#!/usr/bin/python
import re
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
import os

dic_count={}
for line in sys.stdin:
    line = line.strip()
    streetName, num = line.split('\t')
    try:
        num=int(num)
        dic_count[streetName]=dic_count.get(streetName,0)+num
    except ValueError:
        pass


dic=dic_count
##for i in countData:
##    dic[i]=dic.get(i,0)+1
dic=sorted(dic.items(),key=lambda item:item[1],reverse=True)
for i in dic[0:3]:
    print(i)
##print(dic)
