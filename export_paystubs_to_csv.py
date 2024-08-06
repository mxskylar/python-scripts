import pypdf

def main(args):
    pdf_reader = pypdf.PdfReader(args.paystubs.name) 
    print(pdf_reader.pages[0].extract_text())
