##
#       Merges the pdf using third party module PyPDF2.
##      You can do all the text handling like reading from pdf and creating new pdf like that. But, you cant edit existing pdf
##
import PyPDF2
import os

pdfFile = open('112065.pdf', 'rb') # pdf file are binary files
reader = PyPDF2.PdfFileReader(pdfFile)  # returns the reader object which futher has many methods like, numPages(), getpage() etc.

print(reader.numPages)
page = reader.getPage(0) # this returns the 'page' object which has method 'extractText()': This can be used to read the whole page of pdf file. Page number index from 0
print(page.extractText())

# To read all the data in pdf file, use for loop
for pages in range(reader.numPages):
    print(reader.getPage(pages).extractText())
