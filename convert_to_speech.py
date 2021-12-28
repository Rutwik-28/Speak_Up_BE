# import PyPDF2
import pyttsx3

# path of the PDF file
path = open('demofile2.txt', 'rb')

# creating a PdfFileReader object
# pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 25th page.



# 

# speak = pyttsx3.init()
# speak.say(text)
# speak.runAndWait()

f = open('demofile2.txt', 'r')
theText = f.read()
f.close()
pyttsx3.speak.say(theText)
pyttsx3.speak.runAndWait()