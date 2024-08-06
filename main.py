from argparse import ArgumentParser, FileType
import export_paystubs_to_csv

EXPORT_PAYSTUBS_TO_CSV="export_paystubs_to_csv"

if __name__ == "__main__":
    # Global args parser
    parser = ArgumentParser(description="Scripts for personal workflows written in Python")
    subparsers = parser.add_subparsers(dest="command", help="sub-command")
    # export_paystubs_to_csv
    export_paystubs_to_csv_parser = subparsers.add_parser(EXPORT_PAYSTUBS_TO_CSV, help="Export data parsed from paystub PDFs to CSV")
    export_paystubs_to_csv_parser.add_argument("--paystubs", help="PDF with Paystubs to parse", required=True, type=FileType("r"))

    args = parser.parse_args()
    if args.command == EXPORT_PAYSTUBS_TO_CSV:
        export_paystubs_to_csv.main(args)
