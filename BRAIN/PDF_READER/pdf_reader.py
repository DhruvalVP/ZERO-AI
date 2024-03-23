import PyPDF2
import os
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[4].id) 
    engine.setProperty("rate",165)
    engine.say(text)
    engine.runAndWait()

def pdf_reader(filename, read_from_which_page_number=0, startfile=True):
    # Check if the 'startfile' flag is set to True, and if so, open the PDF file using the default viewer.
    if startfile == True:
        os.startfile(filename)

        # Open the PDF file in binary mode for reading.
        book = open(filename, "rb")

        # Create a PdfFileReader object to read the PDF fi le.
        pdf_reader = PyPDF2.PdfFileReader(book)

        # Get the total number of pages in the pdf.
        pages = pdf_reader.getNumPages()
        print("Number of Pages = ", pages)

        # Get the specified page using the provided 'read from _ which _ page number' .
        page = pdf_reader.getPage(read_from_which_page_number)

        try:
            # Extract text from the selected page.
            text = page.extract_text()

            # Close the opened PDF file.
            book.close()

            # return the extracted Text file from the specified page.
            return text
        
        except Exception as e:
            print("Cannot Read PDF!!")
            book.close()
            return None
    

pdf_file = "C:\\Users\\dvpne\\Downloads\\Documents\\The Martian.pdf"
print(pdf_reader(pdf_file))
say(pdf_reader(pdf_file))