import pyttsx3
import PyPDF2

book=open("OSPP-16 Pankaj Sir (Prayas) - OSPP-16_Pankaj Sir_Prayas_31032021.pdf","rb")
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker=pyttsx3.init()
page=pdfReader.getPage(2)
text=page.extractText()

speaker.say(text)
speaker.runAndWait()
