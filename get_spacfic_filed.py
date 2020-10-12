import pdfminer
from cryptography.hazmat.backends import default_backend
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    # study next line who has values StringIO
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open('name.pdf', 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    file1 = open("output.txt","w")
    L = ["This is Delhi \n","This is Paris \n","This is London \n"]

    # \n is placed to indicate EOL (End of Line)
    file1.write(text)
    file1.writelines(L)
    file1.close() #to change file access modes
    #print(text)
    #if 'RUE_PERNON' in text:
        #print("I found RUE_PERNON")
        #print('Now What')
        #print(text)
    result = text.index('CODE  POSTAL')
    print("CODE  POSTAL':", result)
    #len of first cell "CODE  POSTAL':"
    filed_length_name = len("CODE  POSTAL':")
    filed1_result_len = 5
    postal_starting_at = result + filed_length_name
    postal_code_answer = ""
    answers = {}
    for i in range(6):
        postal_code_answer += text[postal_starting_at + i]
    answers['postal_code'] = postal_code_answer
    print(answers['postal_code'])
    ## coninute from here
    print(answers)
    fp.close()
    device.close()
    retstr.close()
    print('h')
    return

if __name__ == '__main__':
    path = 'name.pdf'
    convert_pdf_to_txt(path)
