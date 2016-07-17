#!/usr/bin/python

##
#	@author Livefree
#

filePath = "/home/livefree/Desktop/training_set.tsv"



N = 1

f = open(filePath, "r");
i = 0

 
content = f.readlines(1)


for c in content :
	#contentList = content[1].split('\t')
	contentList = c.split('\t')
	essay = contentList[2]
	score = int(contentList[6])%5
	if score == 0 :
		score = 5
	print essay + "\n" + str(score)

# from itertools import islice
# with open(filePath) as myfile:
#     head = list(islice(myfile, N))

# print head


# i = 0
# with open(filePath) as f:
#     content = f.readlines()
#     i += 1
#     if i >=10 :
#     	break;

#fo = open(filePath, "r")

#essay = sourceFile.read()