import pypdf
import re

OUTPUT_CSV = "output/paystubs.csv"

def main(args):
    with open(OUTPUT_CSV, "w") as file:
        file.write("Federal Withholding,State Withholding")
    pdf_reader = pypdf.PdfReader(args.paystubs.name)
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        matches = re.findall("(((\d|,)+\.\d\d))", page_text)
        if len(matches) >= 30:
            federal_withholding = matches[27][0]
            state_withholding = matches[29][0]
            with open(OUTPUT_CSV, "a") as file:
                file.write(f"\n{federal_withholding},{state_withholding}")
    print(f"✅ Exported paystub data to {OUTPUT_CSV}")
