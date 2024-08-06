import pypdf
import re

OUTPUT_CSV = "output/paystubs.csv"

def main(args):
    with open(OUTPUT_CSV, "w") as file:
        file.write("Federal Withholding,State Withholding")
    pdf_reader = pypdf.PdfReader(args.paystubs.name)
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        match = re.search("Federal Withholding(((\d|,)+\.\d\d))", page_text)
        if match:
            # federal withholding
            print(match.group(1))
            #with open(OUTPUT_CSV, "a") as file:
                #file.write(f"\n{federal_withholding}|{state_withholding}")
    print(f"✅ Exported paystub data to {OUTPUT_CSV}")
