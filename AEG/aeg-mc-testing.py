#!/usr/bin/python

##
#	@author Livefree
#

from Statistics.Statistics import *
from Spellings.Spellings import *
from Grammar.Grammar import *
import sys
import webbrowser
from operator import itemgetter
import os


 # 3.184278 
 # 0.034822 
 # 0.323678 
 # 0.120132 
 # 0.139415 
# values that came from linear regression model
theta = [3.184278 ,0.034822, 0.323678 , 0.120132 ,0.139415 ]

#make dictionary
fo = open("/home/livefree/Desktop/data_test.txt","a+")
print "Please wait the dictionary is getting loaded :: "
makeDictionary()

filePath = "/home/livefree/Desktop/test_set.tsv"

f = open(filePath, "r");
i = 0

numberOfResults = 33

content = f.readlines(30)

while i < 6 :
	i += 1	 
	content = f.readlines(1)

	for c in content :
		#contentList = content[1].split('\t')
		print "The essay to be graded is " + str(numberOfResults) +  " :: \n\n"
		contentList = c.split('\t')
		essay = contentList[2]
		score = int(contentList[6])%5
		if score == 0 :
			score = 5
		#print essay + "\n" + str(score)
		#read essay
		#essay = sourceFile.read()


		print "Please Wait while we generate statistics for your essay........"

		#Statistics
		wordCount = getWordCount(essay)
		beautifulWords = getBeautifulWordCount(essay)
		sentCount = getSentenceCount(essay)
		paraCount = getParaCount(essay)
		avgSentLen = getAvgSentenceLength(essay)
		stdDevSentLen = getStdDevSentenceLength(essay)


		print
		print "Please Wait while we perform spell check on your essay........"

		#Spellings
		numMisspelt, misspeltWordSug = spellCheck(essay)

		print
		print "Please Wait while we analyse the Grammar and Structure of your essay........\n"

		#Grammar
		grammarCumScore, grammarSentScore = getGrammarScore(essay)


		#Overall
		#overallScore = (format((((1-(float(numMisspelt)/wordCount))*5) + grammarCumScore)/2, '.2f'))
		overallScore =  theta[0] + (theta[1] * grammarCumScore) + (theta[2] * sentCount) + (theta[3]*beautifulWords) + (theta[4]*avgSentLen)
		overallScore = overallScore % 10
		print ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

		print "The overallScore of the essay is (1-10) " + str(overallScore) + "\n"

		print "Number of Misspelt Words " + str(numMisspelt) 

		print "Spelling Score (0-5) " +  str((1-(float(numMisspelt)/wordCount))*5)+ "\n"

		print "Grammar(0-5) " + str((grammarCumScore)) 

		print "Word Count " + str(wordCount) 
		print "Beautiful Words Count " + str(beautifulWords) 
		print "Sentence Count " + str(sentCount) 
		print "Paragraph Count " + str(paraCount) 
		print "Average Sentence Length " + str(format(avgSentLen,'.2f')) 
		print "Standard Deviation from the Average Sentence Length " + str(format(stdDevSentLen,'.2f')) 

		#for key in reversed(sorted(list(grammarSentScore.items()), key=itemgetter(1))):
		#	print key[0] + "\t" + str(key[1]) ;

	#	for key in misspeltWordSug:
	#		print key + " " + str(misspeltWordSug[key]) 


		# writing data on the file

		
		dataToBeWritten = str(overallScore) + "\t" + str(score) + "\n";
		numberOfResults += 1
		fo.write(dataToBeWritten);


fo.close()

#/home/livefree/Projects/MajorProject/AEG/Sample_Essays/dog.txt

deleteDictionary()