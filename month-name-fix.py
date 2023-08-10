import re
import shutil

# Dictionary to map month abbreviations to numbers
month_mapping = {
    "jan": "1",
    "feb": "2",
    "mar": "3",
    "apr": "4",
    "may": "5",
    "jun": "6",
    "jul": "7",
    "aug": "8",
    "sep": "9",
    "oct": "10",
    "nov": "11",
    "dec": "12"
}

# Read the content of the original .bib file with UTF-8 encoding
with open("references.bib", "r", encoding="utf-8") as file:
    bib_content = file.read()

# Replace month abbreviations with numbers using regex
for month_abbrev, month_number in month_mapping.items():
    pattern = f'\\b{month_abbrev}\\b'
    replacement = month_number
    bib_content = re.sub(pattern, replacement, bib_content, flags=re.IGNORECASE)

# Write the modified content back to the original .bib file with UTF-8 encoding
with open("references.bib", "w", encoding="utf-8") as file:
    file.write(bib_content)