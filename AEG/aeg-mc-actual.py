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

#values calculated from linear regression
theta = [3.184278 ,0.034822, 0.323678 , 0.120132 ,0.139415 ]


#make dictionary

print "Please wait the dictionary is getting loaded :: "
makeDictionary()

#open essay
print "Enter the name(path) of file containing the Essay to be graded :: "
sourceFileName = str(raw_input(" >> "))
sourceFile = open(sourceFileName, "r")

#sourceFileBaseName = os.path.basename(sourceFileName)
#outputFileName = "./Reports/" + os.path.splitext(sourceFileBaseName)[0] + ".html"

#read essay
essay = sourceFile.read()


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


#print
#print "Please Wait while we analyse the Coherence of your essay........"

#Coherence
#coherenceScore = getCoherenceMeasure(essay)

#Overall
overallScore = (format((((1-(float(numMisspelt)/wordCount))*10) + grammarCumScore)/2, '.2f'))
print ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

print "The overallScore(Static Score) of the essay is (0-10) " + str(overallScore) + "\n";

print "Number of Misspelt Words " + str(numMisspelt) ;

print "Spelling Score (0-5) " +  str((1-(float(numMisspelt)/wordCount))*5)+ "\n"

print "Grammar(0-5) " + str((grammarCumScore)) ;

print "Word Count " + str(wordCount) ;
print "Sentence Count " + str(sentCount) ;
print "Paragraph Count " + str(paraCount) ;
print "Average Sentence Length " + str(format(avgSentLen,'.2f')) ;
print "Standard Deviation from the Average Sentence Length " + str(format(stdDevSentLen,'.2f')) ;

#for key in reversed(sorted(list(grammarSentScore.items()), key=itemgetter(1))):
#	print key[0] + "\t" + str(key[1]) ;

for key in misspeltWordSug:
	print key + " " + str(misspeltWordSug[key]) 


result =  theta[0] + (theta[1] * grammarCumScore) + (theta[2] * sentCount) + (theta[3]*beautifulWords) + (theta[4]*avgSentLen)

print "\n The actual result from the linear regression model is(1-10)  " + str(result%10)

#/home/livefree/Projects/MajorProject/AEG/Sample_Essays/dog.txt
deleteDictionary()