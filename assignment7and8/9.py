import re
punctuations = r'[.,!?;:()]'
date = r'\d{1,2}[-/]\d{1,2}[-/]\d{3,4}|\d{3,4}[-/]\d{1,2}[-/]\d{1,2}[-/]'
urls = r'https?://[^$\s/.?#].[^\s]'
email = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}'
number = r'(\d{1,3}(?:,\d{3})*(?:.\d{1,2})?)'
social_ids = r'@[a-zA-Z0-9_]+'
telugu_text = r'[\u0c00-\u0c7F]+'
pattern = [punctuations,date,urls,email,number,social_ids,telugu_text]
combined_pattern = '|'.join(pattern)
def tokenizer(text):
    tokens = []
    for patterns in pattern:
        matches = re.findall(patterns,text)
        tokens.extend(matches)
    return tokens
text = '''తెలుగు భాష అనేది భారతదేశంలోని ప్రాచీన భాషలలో ఒకటి మరియు ఇది ద్రావిడ భాషా కుటుంబానికి చెందినది.
'''
tokens = tokenizer(text)
print(tokens)          