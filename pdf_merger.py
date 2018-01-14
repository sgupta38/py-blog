##      Author: Sonu Gupta
##
#       Purpose: Merges the pdf using third party module PyPDF2.[pip install PyPDF2]
##
import PyPDF2
import os

filesList = []
finalpdfFile = open('final_merged.pdf', 'wb')
writer = PyPDF2.PdfFileWriter()

print('How many files you want to merge?')
totalFiles = input()

for i in range(int(totalFiles)):
    print('Enter the full path of the file.')
    fileName = input()
    filesList.append(fileName)

for filename in filesList:
    pdfFile = open(filename, 'rb')
    reader = PyPDF2.PdfFileReader(pdfFile)

    #Reading indivisual page and adding the same to writer object.
    for pageNum in range(reader.numPages):
        page =  reader.getPage(pageNum)
        writer.addPage(page)
        writer.write(finalpdfFile)

    pdfFile.close()

finalpdfFile.close()
