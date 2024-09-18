from collections import Counter
import csv

# Open and read the consolidated text file
with open('consolidated_text.txt', 'r') as file:
    text = file.read()

# Tokenize the text into words (split by whitespace)
words = text.split()

# Count the occurrences of each word
word_count = Counter(words)

# Get the top 30 most common words
top_30_words = word_count.most_common(30)

# Save the top 30 words into a CSV file
with open('top_30_words.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Word', 'Count'])
    writer.writerows(top_30_words)

print("Top 30 words successfully written to 'top_30_words.csv'")

