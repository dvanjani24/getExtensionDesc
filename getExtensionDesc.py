import os, re
from statistics import mean

def getExtensionDesc(dir):
    file_list = []
    ext = []
    for root, dirs, files in os.walk(dir):
        for file in files:
        	file_list.append(os.path.join(root, file))
        	ext += [os.path.splitext(file)[1]]
    ext = set(ext)      
    d = dict()
    for i in ext:
    	if "." not in i:
    		continue
    	d[i] = {}
    	temp = [] 
    	for j in file_list: 
    		if i in j:
    			temp += [os.path.getsize(os.path.join(root, j))]
    	d[i] = {'Count':len(temp),'Min':min(temp), 'Avg':mean(temp), 'Max':max(temp)}		
    return d
#print(getExtensionDesc(os.getcwd()))