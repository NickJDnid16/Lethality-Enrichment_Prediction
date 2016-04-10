
import sys
import codecs
from itertools import repeat
import csv

from Ontology_Attributes import *
from Single_Lethalities import *


#Create Ontology File
ontology_attributes()

#Single Lethality Genes
single_lethalities()
#
# PhenLines = []
# inputfile = open('./allele_phenotypic_data_fb_2015_04.tsv', mode='rb')
#
# AL_Rows = []
#
# for line in inputfile:
#     if "FB" in line:
#         PhenLines.append(line)
#
# inputfile.close()
#
#
#
#
# input = csv.reader(PhenLines, delimiter='\t')
#
#
#
# for i, row in enumerate(input):
#     if i == 0:
#         pass
#     else:
#         count = int (1)
#         del row[1]
#         if count > 0:
#
#             AL_Rows.append(repeat(row[0:2], count))
#
# print "Hello"
# ##################################################
#
# outputfile = open('./Removed_Partial_Lethality.txt', mode='wb')
#
# P_Temp = []
# W_Temp = []
#
# RPL = []
#
# for line in AL_Rows:
#     p = "partially"in line
#     if not p:
#         print (line)
#         P_Temp.append(line)
#
# for line in P_Temp:
#     v = "viable" in line
#     w = "with" in line
#     if (v and w):
#         W_Temp.append(line)
#     elif (not w):
#         print(line)
#         W_Temp.append(line)
#
#
# for line in W_Temp:
#     if "viable" in line and "poor" in line:
#         RPL.append(line)
#     elif not "poor" in line :
#         print(line)
#         RPL.append(line)
#
# outputfile.close()
#
#
# inputfile = open('./Removed_Partial_Lethality.txt', mode='rb')
# outputfile = open('./Gene&Lethality_Only.txt', mode='wb')
#
# inputfile = csv.reader(inputfile, delimiter=',')
#
# for row in inputfile:
#
#
#     #del row[1]
#     Temp = (str(row[0]))
#     Temp = Temp.split('[')[0].strip()
#     #Temp = Temp.replace(',','')
#     print Temp
#     print
#     outputfile.write(Temp)
#     outputfile.write(',')
#     outputfile.write(str(row[1]))
#     outputfile.write('\n')
#
#
# #############################################################
#
#
# inputfile = open('./Gene&Lethality_Only.txt', mode='rb')
# outputfile = open('./Gene_With_Lethal&Viable_Only.txt', mode='wb')
#
# inputfile = csv.reader(inputfile, delimiter=',')
#
# for row in inputfile:
#
#
#     #del row[1]
#     Temp = (str(row[1]))
#     if "lethal" in Temp:
#         Temp = "lethal"
#     elif "viable" in Temp:
#         Temp = "viable"
#     else:
#         Temp = "other"
#
#
#     outputfile.write(str(row[0]))
#     outputfile.write(",")
#     outputfile.write(Temp)
#     outputfile.write('\n')
#
# #############################################################
#
#
# data = {}
#
# ##########################################
# inputfile = open('./Gene_With_Lethal&Viable_Only.txt', mode='rb')
# outputfile = open('./Genes_With_All_Lethality.txt', mode='wb')
#
# for line in inputfile:
#     split_string = line.split(",")
#     genome = split_string [0]
#     lethalNotation = split_string [1]
#     data [genome] = data.get(genome,"")+lethalNotation.rstrip('\r\n')+","
#
#
# for x in data:
#     outputfile.write(x+","+data[x]+"\n")
#
# outputfile.close()
#
#
#
# ########################################
#
#
#
#
#
#
# outputfile = open('./Single_Lethality_Genes.txt', mode='wb')
# inputfile = open('./Genes_With_All_Lethality.txt', mode='rb')
# essOutputfile = open('./Lethal_Fly.txt', mode='wb')
#
#
# for line in inputfile:
#     v = "viable" in line
#     l = "lethal" in line
#     o = "other" in line
#
#
#     if (l and v):
#         print ("Ignoring Line")
#     else:
#         line = line.rstrip()
#         bits = line.split(',')
#         if(v) or (o) and not (l):
#             bit = bits[0]+",viable\n"
#             print (bit)
#             outputfile.write(bit)
#         elif(l) and (o):
#             bit = bits[0]+",lethal\n"
#             print (bit)
#             outputfile.write(bit)
#             essOutputfile.write(bits[0] + "\n")
#         elif(l) and not (v):
#             bit = bits[0]+",lethal\n"
#             print (bit)
#             outputfile.write(bit)
#             essOutputfile.write(bits[0] + "\n")
#         elif ((not l) and (not v) and (not o)):
#             print("Not Viable OR Lethal")
#
# outputfile.close()
#

############################################################################################


