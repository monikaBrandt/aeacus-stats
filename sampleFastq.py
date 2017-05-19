from Bio import SeqIO
import sys
import numpy
import pandas as pd

def parseFastq(filen,nr):
    si=1
    for record in SeqIO.parse(filen, "fastq"):#This loop is per read, not per row.
        if si % 10 == 0:
            print(si)
            getQscore(record.seq,record.letter_annotations["phred_quality"])
        si+=1

def getQscore(seq,qscore):
    print seq,qscore   
    for i in range(0, len(seq)):
        print(qScorePerBasePosA[i+1])
        if seq[i] == 'A':
            print(i)
            print(i+1)
            print(qscore[i])
            qScorePerBasePosA[i+1].append(qscore[i])
            print(qScorePerBasePosA[i+1])
        else:
            qScorePerBasePosA[i+1]#.append(None)
    

def calculateQStats(nframe):
    nmean = nframe.apply(numpy.mean,axis=0)
    nstd = nframe.apply(numpy.std,axis=0)
    statsPerBasePosN = dict.fromkeys(range(1,readlen+1),list())
    return(statsPerBasePosN)
    
filename=sys.argv[1]#fastq filename
print(filename)
nrow=sys.argv[2]#number of rows in fastq file
print(nrow)
readlen=151
qScorePerBasePosA = dict.fromkeys(range(1,readlen+1),list())
print(qScorePerBasePosA)
parseFastq(filename,nrow)
#print(qScorePerBasePosA)
#aframe = pd.DataFrame.from_dict(qScorePerBasePosA,orient='columns')
#print(aframe)
#meanstda=calculateQStats(aframe)
#print(meanstda)

