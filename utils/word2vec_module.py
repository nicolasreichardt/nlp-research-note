from gensim.models import Word2Vec, KeyedVectors
import numpy as np

class Word2VecModel:
    def __init__(self, vector_size=100, window=5, min_count=1, workers=4):
        """
        Initialize the Word2Vec model with the given parameters.
        """
        self.vector_size = vector_size
        self.window = window
        self.min_count = min_count
        self.workers = workers
        self.model = None

    def _get_keyed_vectors(self):
        """
        Get the KeyedVectors object from the model.
        Works with both Word2Vec models and standalone KeyedVectors.
        """
        if self.model is None:
            return None
        if isinstance(self.model, KeyedVectors):
            return self.model
        elif hasattr(self.model, 'wv'):
            return self.model.wv
        return None

    def train(self, sentences):
        """
        Train the Word2Vec model on the provided sentences.
        :param sentences: List of tokenized sentences.
        """
        self.model = Word2Vec(
            sentences=sentences,
            vector_size=self.vector_size,
            window=self.window,
            min_count=self.min_count,
            workers=self.workers
        )

    def save(self, filepath):
        """
        Save the trained Word2Vec model to the specified filepath.
        :param filepath: Path to save the model.
        """
        if self.model:
            if isinstance(self.model, KeyedVectors):
                self.model.save(filepath)
            else:
                self.model.save(filepath)
        else:
            raise ValueError("Model has not been trained yet.")

    def load(self, filepath):
        """
        Load a Word2Vec model from the specified filepath.
        :param filepath: Path to load the model from.
        """
        try:
            self.model = Word2Vec.load(filepath)
        except Exception:
            self.model = KeyedVectors.load(filepath)

    def get_vector(self, word):
        """
        Get the vector representation of a word.
        :param word: Word to retrieve the vector for.
        :return: Vector representation of the word.
        """
        kv = self._get_keyed_vectors()
        if kv is not None and word in kv:
            return kv[word]
        return None

    def most_similar(self, word, topn=5):
        """
        Find the most similar words to a given word.
        :param word: The target word.
        :param topn: Number of similar words to return.
        :return: List of (word, similarity) tuples.
        """
        kv = self._get_keyed_vectors()
        if kv is not None and word in kv:
            return kv.most_similar(word, topn=topn)
        else:
            raise KeyError(f"Word '{word}' not in vocabulary or model not loaded.")

    def similarity(self, word1, word2):
        """
        Compute cosine similarity between two words.
        :param word1: First word.
        :param word2: Second word.
        :return: Similarity score.
        """
        kv = self._get_keyed_vectors()
        if kv is not None and word1 in kv and word2 in kv:
            return kv.similarity(word1, word2)
        else:
            raise KeyError(f"One or both words not in vocabulary or model not loaded.")

    def document_vector(self, tokens):
        """
        Compute the average vector representation of a document.
        :param tokens: List of tokens in the document.
        :return: Average vector of the document.
        """
        kv = self._get_keyed_vectors()
        if kv is None:
            raise ValueError("Model has not been trained or loaded yet.")
        
        vectors = [kv[token] for token in tokens if token in kv]
        
        if vectors:
            return np.mean(vectors, axis=0)
        else:
            return np.zeros(self.vector_size)

    def cosine_similarity(self, vec1, vec2):
        """
        Compute cosine similarity between two vectors.
        """
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)

    def most_similar_to_document(self, tokens, topn=5):
        """
        Find words most similar to a document.
        """
        kv = self._get_keyed_vectors()
        if kv is None:
            raise ValueError("Model has not been trained or loaded yet.")
        doc_vector = self.document_vector(tokens)
        return kv.similar_by_vector(doc_vector, topn=topn)