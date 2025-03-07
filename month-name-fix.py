import re

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

# Replace month abbreviations with numbers using a single regex
pattern_month = r'month\s*=\s*{([a-z]+)},'
def replace_month(match):
    month_abbrev = match.group(1)
    month_number = month_mapping.get(month_abbrev, month_abbrev)
    return f'month = {{{month_number}}},'

modified_content = re.sub(pattern_month, replace_month, bib_content, flags=re.IGNORECASE)

# Replace "%" with "\%" when not preceded by a backslash
modified_content = re.sub(r'(?<!\\)%', r'\\%', modified_content)

# Replace "&" with "\&" when not preceded by a backslash
modified_content = re.sub(r'(?<!\\)&', r'\\&', modified_content)

# Write the modified content back to the original .bib file with UTF-8 encoding
with open("references.bib", "w", encoding="utf-8") as file:
    file.write(modified_content)
    
print("done")
