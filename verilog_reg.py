#!/usr/bin/python3

import os
import re
import sys
import openyxl import Workbook

workbook = Workbook()
sheet = workbook.active
pattern =r"(\breg\b)((.+\[\w+-\d:\d\])|)(\W+)(\w+)((\s\[\w+-\d:\d\])|)(;)"

directory = sys.argv[1]

files = os.listdir(directory)


def rtl_reg(file_name):
    with open(file_name,'r') as file:
        for line in file.readlines():
            match = re.search(pattern,line)
            if match:
                reg_name = match.group(5)
                print("The Register in the file ---> [" + file_name+"] are: \n ")
                print("REG NAME -->"+ reg_name)





for each_file in files:
    x = each_file.split(".")
    if x[1] == 'v' or x[1] == 'sv':
        print(each_file)
        rtl_reg(each_file)
