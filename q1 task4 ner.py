import spacy

# Load the biomedical NER model from scispaCy
nlp = spacy.load("en_ner_bc5cdr_md")

# Increase the maximum length SpaCy will accept
nlp.max_length = 1500000  # Adjust this limit as needed

# Open and read the consolidated text file
with open('consolidated_text.txt', 'r') as file:
    text = file.read()

# Process the text using the NER model
doc = nlp(text)

# Extract entities related to diseases and drugs
entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['DISEASE', 'DRUG']]

# Print out the extracted entities
for entity in entities:
    print(entity)

