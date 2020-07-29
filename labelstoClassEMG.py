#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:53:08 2020

@author: michael
"""

import os, sys
import numpy as np
import matplotlib.pyplot as plt
import csv

def numtoClass(input_file, output_file):
    with open((output_file),'w',newline='') as csvfile:
        emgwriter=csv.writer(csvfile, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_data = np.genfromtxt(input_file, delimiter=',')
        dataset = csv_data[1:,0:-1]
        labels = csv_data[1:,-1]
        with open(input_file) as readheads:
            headers=csv.DictReader(readheads).fieldnames
        #headers = csv_data.dtype.names
        #Class=[]
        index=0
        headers=headers[:-1]
        headers.append('Class')
        emgwriter.writerow(tuple(list(headers)))
        for x in labels:
            datarow=dataset[index]
            writerow=list(datarow)
            if x==0:
                #Class.append('Open') # or sometimes Splay
                """commenting out this unused approach.
                will look again later as it might actually be better"""
                writerow.append('Open')
            elif x==1:
                #Class.append('Neutral')
                writerow.append('Neutral')
            elif x==2:
                #Class.append('Close') # or sometimes Clench
                writerow.append('Close')
            elif x==3:
                #Class.append('Scissors') # or sometimes Peace
                writerow.append('Scissors')
            elif x==4:
                #Class.append('ThumbsUp')
                writerow.append('ThumbsUp')
            elif x==5:
                #Class.append('Paper') # or sometimes FlatOpen
                writerow.append('Paper')
            elif x==6:
                #Class.append('IdxPoint')
                writerow.append('IdxPoint')
            elif x==7:
                #Class.append('FlatClose')
                writerow.append('FlatClose')
            elif x==8:
                #Class.append('FingerGun')
                writerow.append('FingerGun')
            elif x==9:
                #Class.append('waveout') # or sometimes openout
                writerow.append('waveout')
            elif x==10:
                #Class.append('wavein') # or sometimes openin
                writerow.append('wavein')
            elif x==11:
                #Class.append('closeout')
                writerow.append('closeout')
            elif x==12:
                #Class.append('closein')
                writerow.append('closein')
            else:
                #Class.append('Undefined')
                writerow.append('Undefined')
            writerow=tuple(writerow)
            emgwriter.writerow(writerow)
            index=index+1
        print('conversion success')
        #emgwrite=list(emg)
        #emgwrite.append(int(round(time.time() * 1000)))
        #emgwrite=tuple(emgwrite)
        #emgwriter.writerow(emgwrite)


if __name__ == '__main__':
	if len(sys.argv) <3:
		print ('arg1: input dir\narg2: output file')
		sys.exit(-1)
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	numtoClass(input_file, output_file)