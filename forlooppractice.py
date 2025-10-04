# Oct2024 to practice for pdf renaming

import glob
import os
import re
from pathlib import Path
from pypdf import PdfReader

output_folder = Path('/spam/eggs/folder/')

regex = r'[0-9]{5,6}'


""" # below is good for printing but doesn't rename 
for filename in glob.glob('/spam/eggs/folder/Intact_202509*.pdf'):
reader = PdfReader(filename)
    page = reader.pages[0]
    regex_invoice_number = re.search(regex, page.extract_text()).group()
    if len(regex_invoice_number) == 6:
        print(regex_invoice_number)
    elif len(regex_invoice_number) == 5:
        print(regex_invoice_number+"-credit")
"""

for filename in glob.glob('/spam/eggs/folder/Intact_202509*.pdf'):
    reader = PdfReader(filename)
    page = reader.pages[0]
    regex_invoice_number = re.search(regex, page.extract_text()).group()
    if len(regex_invoice_number) == 6:
        os.rename(filename, output_folder/regex_invoice_number)
    elif len(regex_invoice_number) == 5:
        os.rename(filename, output_folder/(str(regex_invoice_number)+"-credit"))

# ok so that works, note to add word to filename needs whole thing
# turned into a string
