import pypdf
import re

def main(args):
    pdf_reader = pypdf.PdfReader(args.paystubs.name) 
    page_text = pdf_reader.pages[0].extract_text()
    if match := re.search(".+Federal Withholding((\d|,)+\.\d\d)State Tax - MA(.+)Earnings.+", page_text):
        print(match.group(1))
        print(match.group(2))
