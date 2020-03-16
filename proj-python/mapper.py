#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
import os

##
##pat = re.compile("(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\D.*?\d{4}:(?P<hour>\d{2}):\d{2}.*?")
##for line in sys.stdin:
##    match = pat.search(line)
##    if match:
##        print '%s\t%s' % (match.group('hour')+' '+match.group('ip'),1)
##

data=pd.read_csv("Parking_Violations_Issued_-_Fiscal_Year_2020.csv")

countData=data['Street Name'].tolist()

for line in countData:
    print '%s\t%s' % (line,1)
