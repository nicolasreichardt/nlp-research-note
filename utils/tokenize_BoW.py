
# Custom tokenization function
def custom_tokenizer(text): # wrap tokenizer in custom function
    tokenized_text = nlp(text)
    return [tok.text.strip() for tok in nlp(text) if tok.text.strip() !=''] #return [tok.text for tok in tokenized_text]