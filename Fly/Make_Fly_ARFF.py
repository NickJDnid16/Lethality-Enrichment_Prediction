import sys
import codecs
from itertools import repeat
import csv


PhenLines = []
inputfile = open('./allele_phenotypic_data_fb_2015_04.tsv', mode='rb')
print "1"
AL_Rows = []

for line in inputfile:
    if "FB" in line:
        PhenLines.append(line)

inputfile.close()




input = csv.reader(PhenLines, delimiter='\t')



for i, row in enumerate(input):
    if i == 0:
        pass
    else:
        count = int (1)
        del row[1]
        if count > 0:

            AL_Rows.append(repeat(row[0:2],count))

print "1"
##################################################

print "2"
AL_Rows = map(str, AL_Rows)

P_Temp = []
W_Temp = []

RPL = []

p = "partially" in line
v = "viable" in line
w = "with" in line
for line in AL_Rows:
    if "partially" not in line:
        P_Temp.append(line)


for line in P_Temp:

    if "viable" in line and "with" in line:
        W_Temp.append(line)
    elif not "with" in line:
        W_Temp.append(line)
#######################Are the 'Withs' Getting removed correctly?


for line in W_Temp:
    if "viable" in line and "poor" in line:
        RPL.append(line)
    elif not "poor" in line :

        RPL.append(line)

print "2"





GLO = []

input = csv.reader(RPL, delimiter=',')
print "3"
for row in input:



    Temp = (str(row[0]))
    Temp = Temp.split("'")[1].strip()
    Temp = Temp.split('[')[0].strip()
    if "viable" in row[1]:
        row[1] = "viable"
    elif "lethal" in row[1]:
        row[1] = "lethal"
    else:
        row[1] = "other"


    print
    GLO.append(Temp+','+str(row[1]))



#############################################################







input = csv.reader(GLO, delimiter=',')

data = {}
GAL = []



for line in input:
    genome = line[0]
    lethalNotation = line[1]
    data [genome] = data.get(genome,"")+lethalNotation+","

outputfile = open('./Test.txt', mode='wb')
for x in data:
    GAL.append(x+","+data[x]+"\n")
    outputfile.write(x+","+data[x]+"\n")





########################################





input = csv.reader(GAL, delimiter=',')

outputfile = open('./Single_Lethality_Genes.txt', mode='wb')

essOutputfile = open('./Lethal_Fly.txt', mode='wb')


for line in input:
    v = "viable" in line
    l = "lethal" in line
    o = "other" in line


    if (l and v):
        print ("Ignoring Line")
    else:

        if(v) or (o) and not (l):
            bit = line[0]+",viable\n"
            print (bit)
            outputfile.write(bit)
        elif(l) and (o):
            bit = line[0]+",lethal\n"
            print (bit)
            outputfile.write(bit)
            essOutputfile.write(line[0] + "\n")
        elif(l) and not (v):
            bit = line[0]+",lethal\n"
            print (bit)
            outputfile.write(bit)
            essOutputfile.write(line[0] + "\n")
        elif ((not l) and (not v) and (not o)):
            print("Not Viable OR Lethal")

outputfile.close()

sys.exit("SDSD") #### Still problems.. mel]" should be mel - check singleleth Genes
############################################################################################

__author__ = 'nid16'

import codecs
import csv
import sys
data = {}
import pprint
outputfile = open('./Gene&GO_F.txt', mode='wb')
GOoutputfile = open('./Gene_With_Only_GO.txt', mode='wb')

Seen =[]


geneAssociation = open('./gene_association.fb', mode='rb')

for line in geneAssociation:
    split_string = line.split("\t")
    if(split_string[0] == "FB"):#FlyBase = FB
        genome = split_string[2]
        print genome
        GO = split_string[4]
        dataMarker = split_string[6]
        data[genome] = data.get(genome,"")+GO+","+dataMarker+","
        if genome not in Seen:
            Seen.append(genome)
            GOoutputfile.write(genome + "\n")

for line in open('./Single_Lethality_Genes.txt', mode='rb'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    data[gene] = data.get(gene,"")+str(split_line[1])


########################################################

for x in data:
    print (x,data[x])
    outputfile.write(x+","+data[x]+"\n")
  #  FUNCoutputfile.write()
outputfile.close()


########################################################


inputfile = open('./Gene&GO_F.txt', mode='rb')
outputfile = open('./Gene&GO_F_With_Lethality.txt', mode='wb')
LethalOutput = open('./Lethal_Fly.txt', mode='wb')
Viable_LethalOutput= open('./Lethal&Viable_Fly.txt', mode='wb')
inputfile = csv.reader(inputfile, delimiter=',')

previous = None

writer = csv.writer(outputfile)
Lethalwriter = csv.writer(LethalOutput)
VLwriter = csv.writer(Viable_LethalOutput)

for rows in inputfile:

        if "viable" in str(rows[-1]) or "lethal" in str(rows[-1]):

            if "GO" in str(rows):
                writer.writerow(rows)
                VLwriter.writerow(rows[0:1])
                if "lethal" in str(rows[-1]):
                    Lethalwriter.writerow(rows[0:1])

                print rows

