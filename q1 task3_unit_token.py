from transformers import AutoTokenizer

# Load a pretrained tokenizer from HuggingFace
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Open and read the consolidated text file
with open('consolidated_text.txt', 'r') as file:
    text = file.read()

# Tokenize the text
tokens = tokenizer.tokenize(text)

# Count the unique tokens
unique_tokens = set(tokens)

# Print the top 30 unique tokens
print("Top 30 unique tokens:", list(unique_tokens)[:30])

