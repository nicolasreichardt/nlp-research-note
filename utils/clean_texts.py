import re

def clean_EU_legal_text(text):
    """
    Clean extracted legal document text by removing unnecessary elements
    and normalizing formatting.
    """
    
    # Fix encoding issues like â€™ (should be apostrophe)
    text = re.sub(r'â€™', "'", text)
    text = re.sub(r'â€œ', '"', text)
    text = re.sub(r'â€', '"', text)
    text = re.sub(r'â€"', '—', text)
    text = re.sub(r'â€"', '–', text)
    text = re.sub(r',Äô', '\'', text)
    text = re.sub(r',Äò', '\'', text)    

    
    # Remove "Having regard to..." sections
    text = re.sub(r'Having regard to[^,\n]+[,\n]', '', text, flags=re.IGNORECASE)
    
    # Remove "After transmission..." line
    text = re.sub(r'After transmission[^\n]+\n', '', text, flags=re.IGNORECASE)
    
    # Remove "Acting in accordance..." line
    text = re.sub(r'Acting in accordance[^\n]+\n', '', text, flags=re.IGNORECASE)
    
    # Remove "Where reference is made to..." procedural text
    text = re.sub(r'Where reference is made to this paragraph[^.]+\.', '', text)
    
    # Remove footnote references like (1), (2), (3), (4) but keep article references
    text = re.sub(r'(?<!\d)\s*\((\d{1,2})\)(?!\s*[A-Z])', '', text)
    
    # Remove OJ (Official Journal) references - more comprehensive
    text = re.sub(r'OJ\s+[LC]\s+\d+[^.\n]+\.', '', text)
    text = re.sub(r'\(OJ\s+[LC][^)]+\)', '', text)
    
    # Remove ELI reference
    text = re.sub(r'ELI:\s*http[^\s]+', '', text)
    
    # Remove "Position of the European Parliament..." text
    text = re.sub(r'Position of the European Parliament[^.]+\.', '', text)
    
    # Remove document header/footer patterns
    text = re.sub(r'Offi?cial Jour?nal\s*', '', text)
    text = re.sub(r'of the European Union\s*EN\s*', '', text)
    text = re.sub(r'EN\s+OJ\s+L,\s+\d+\.\d+\.\d+', '', text)
    text = re.sub(r'OJ\s+L,\s+\d+\.\d+\.\d+\s+EN', '', text)
    text = re.sub(r'L series\s*', '', text)
    text = re.sub(r'\d{4}/\d+\s+\d{1,2}\.\d{1,2}\.\d{4}', '', text)
    text = re.sub(r'^\d+/\d+\s*', '', text, flags=re.MULTILINE)
    
    # Remove page numbers like "1/144", "2/144"
    text = re.sub(r'\b\d+/\d+\b', '', text)
    
    # Remove "(Text with EEA relevance)"
    text = re.sub(r'\(Text with EEA relevance\)', '', text)
    
    # Normalize multiple spaces to single space
    text = re.sub(r' +', ' ', text)
    
    # Normalize multiple newlines to double newline (paragraph breaks)
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    
    # Remove spaces before punctuation
    text = re.sub(r' +([,;:.!?])', r'\1', text)
    
    # Fix common spacing issues around parentheses
    text = re.sub(r'\s+\(', ' (', text)
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s+\)', ')', text)
    
    # Strip leading/trailing whitespace from each line
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    
    # Remove empty lines at start and end
    text = text.strip()
    
    # Remove lines that are only numbers or page markers
    lines = [line for line in text.split('\n') 
             if not re.match(r'^\d+', line.strip())]
    text = '\n'.join(lines)
    
    return text

def clean_US_legal_text(text):
    """
    Clean extracted US legal document text by removing unnecessary elements
    and normalizing formatting.
    """

    # --- Cleaning patterns ---
    clean_patterns = [
        # Remove 'VerDate ...' lines
        r"VerDate\s+[A-Za-z0-9<>\s:,.-]+",
        # Remove Federal Register formatting metadata (e.g., PO, Frm, Fmt, Sfmt)
        r"PO\s+\d{5,}|Frm\s+\d+|Fmt\s+\d+|Sfmt\s+\d+",
        # Remove Y:\ file paths and similar
        r"Y:\\SGML\\[A-Za-z0-9_.]+",
        # Remove lines containing code-like CFR references or production notes
        r"rmajette\s+on\s+\S+",
        # Remove redundant whitespace and line breaks
        r"\s{2,}",
        r"\\SGML\\\d+\.XXX\s*\d+",
        r"\bRFC\b",
        r"\bhtiw\b",
        r"DORP3YLW3NJPAL",
        r"\bno\b(?=\s+ettejamr)",
        r"ettejamrExecutive Orders EO \d+"
    ]

    # Apply all cleaning patterns
    for pattern in clean_patterns:
        text = re.sub(pattern, " ", text)

    # Remove multiple line breaks and normalize spacing
    text = re.sub(r"\n+", "\n", text)           # collapse extra newlines
    text = re.sub(r"[ \t]+", " ", text).strip()  # normalize spaces

    return text