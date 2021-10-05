#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TracerPacer

Created on Thu Sep 23 16:51:25 2021

@author: Nooreldean Koteb
"""

import subprocess
import tempfile
import re
from datetime import date
today = date.today()
date = today.strftime("%m/%d/%Y")
targets = {
    'www.gmu.edu':None,
    'www.gwu.edu':None,
    'www.georgetown.edu':None,
    'www.cs.ucla.edu':None,
    'www.wustl.edu':None,
    }

f = open("traceroutes.txt", "a")
id = 1
for target in targets.keys():
    id+=1
    print('Traceroute: ' + target)
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(['traceroute', target], stdout=tempf)
        proc.wait()
        tempf.seek(0)
        lines = tempf.readlines()
        
        newLines = []
        for line in range(len(lines)):
            temp = str(lines[line])[:-3].split(' ')
            
            if '*' in temp:
                pass
            
            else:
                new = []
                for item in temp:
                    item = re.sub("b'", '', item)
                    if item not in ['', 'ms']:
                        if '(' in item:
                            item = item[1:-1]
                        new.append(item)
                newLines.append(new)
        newLines = newLines[1:]
        
        final = []
        for line in newLines:
            if len(line) <= 6:
                final.append(date+','+target+','+str(id)+','+line[0]+','+line[1]+','+line[2]+','+str("{0:.6f}".format(float(line[3])/1000)))
                final.append(date+','+target+','+str(id)+','+line[0]+','+line[1]+','+line[2]+','+str("{0:.6f}".format(float(line[4])/1000)))
                final.append(date+','+target+','+str(id)+','+line[0]+','+line[1]+','+line[2]+','+str("{0:.6f}".format(float(line[5])/1000)))
            else:
                final.append(date+','+target+','+str(id)+','+line[0]+','+str(line[1:]))
                print(f'Warning: {target} ID:{id} Hop:{line[0]} Has more than one reply')   
    
    targets[target] = final
    for line in final:
        f.write(line+'\n')

f.close()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
