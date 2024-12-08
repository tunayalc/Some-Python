import stanza
import pandas as pd

# Download and initialize the Turkish language model for Stanza
stanza.download('tr')
nlp = stanza.Pipeline('tr')

# Read the Excel file
excel = r'C:\Users\ytuna\Downloads\Tunahan Yalçın - data.xlsx'  
df = pd.read_excel(excel)

# Function to find the most common lemma (word root) in a column
def find_most_common_lemma(column):
    word_counts = {}
    for text in column:
        doc = nlp(text)  # Process the text
        
        for sentence in doc.sentences:
            for word in sentence.words:
                lemma = word.lemma  # Get the lemma (word root)
                if len(lemma) > 3:  # Only consider lemmas with more than 3 characters
                    if lemma in word_counts:
                        word_counts[lemma] += 1
                    else:
                        word_counts[lemma] = 1

    # Find the most frequent lemma
    most_common_lemma = max(word_counts, key=word_counts.get)
    return most_common_lemma

# Find and print the most common lemma for each column in the Excel file
for column in df.columns:
    most_common_lemma = find_most_common_lemma(df[column].apply(str))  
    print(f"The most common lemma for column '{column}' is: {most_common_lemma}")
