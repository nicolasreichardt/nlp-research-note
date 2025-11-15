import os
from sklearn.feature_extraction.text import TfidfVectorizer

def load_text(file_path):
    """Load text from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def compute_tfidf(texts):
    """
    Compute TF-IDF scores for a list of texts.
    
    Args:
        texts (list of str): List of cleaned text documents.
    
    Returns:
        tuple: (feature_names, tfidf_matrix)
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    return feature_names, tfidf_matrix

def save_tfidf_values(output_dir, feature_names, tfidf_matrix):
    """
    Save TF-IDF values and their scores to text files.
    
    Args:
        output_dir (str): Directory to save the TF-IDF values.
        feature_names (list of str): List of feature names.
        tfidf_matrix (scipy.sparse.csr_matrix): TF-IDF scores matrix.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for doc_idx, row in enumerate(tfidf_matrix):
        output_file = os.path.join(output_dir, f"tfidf_doc_{doc_idx + 1}.txt")
        with open(output_file, 'w', encoding='utf-8') as file:
            for col_idx in row.nonzero()[1]:
                token = feature_names[col_idx]
                score = row[0, col_idx]
                file.write(f"{token}: {score:.4f}\n")
        print(f"TF-IDF values saved to: {output_file}")

if __name__ == "__main__":
    # Paths to the cleaned text files
    text_file_1 = "data/extracted_text/cleaned_text_1.txt"
    text_file_2 = "data/extracted_text/cleaned_text_2.txt"
    
    # Load the cleaned texts
    text1 = load_text(text_file_1)
    text2 = load_text(text_file_2)
    
    if text1 and text2:
        # Compute TF-IDF
        feature_names, tfidf_matrix = compute_tfidf([text1, text2])
        
        # Save TF-IDF values
        output_directory = "data/tfidf_values"
        save_tfidf_values(output_directory, feature_names, tfidf_matrix)