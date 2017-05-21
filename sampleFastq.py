from Bio import SeqIO
import sys
import numpy
import pandas as pd

def parseFastq(filen,nr):
    sampleDict={}
    si=1
    for record in SeqIO.parse(filen, "fastq"):#This loop is per read, not per row.
        if si % 10 == 0:
            #print(si)
            scoreList=getQscore(record.seq,record.letter_annotations["phred_quality"])
            sampleDict[str(si)] = scoreList
        si+=1
    return sampleDict

def getQscore(seq,qscore):
    print seq,qscore
    readnScores=list()   
    for i in range(1, len(seq)+1):
        if seq[i-1] == 'A':
            #qScorePerBasePosA[i].append(qscore[i-1])
            readnScores.append(qscore[i-1])
            print(qscore[i-1])
        else:
            #qScorePerBasePosA[i].append(None)
            readnScores.append(None)
            print None
    return readnScores
    

def calculateQStats(nframe):
    nmean = nframe.apply(numpy.mean,axis=0)
    nstd = nframe.apply(numpy.std,axis=0)
    #statsPerBasePosN = dict.fromkeys(range(1,readlen+1),list())
    #return(statsPerBasePosN)
    print nmean
    print nstd
    
filename=sys.argv[1]#fastq filename
nrow=sys.argv[2]#number of rows in fastq file
readlen=151
qScorePerBasePosA = dict.fromkeys(range(1,readlen+1),list())
print(qScorePerBasePosA)
smpD = parseFastq(filename,nrow)
#seqstr='NCCACATTTTCAAGAT'
#scorenr=[2, 12, 32, 32, 37, 37, 41, 37, 41, 41, 41, 41, 37, 37, 41, 41]
#print(qScorePerBasePosA)
aframe = pd.DataFrame(smpD)
print(aframe)
trframe=pd.DataFrame.transpose(aframe)
print(trframe)
calculateQStats(trframe)


