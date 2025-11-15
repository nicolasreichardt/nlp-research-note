from gensim.models import Word2Vec

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
            self.model.save(filepath)
        else:
            raise ValueError("Model has not been trained yet.")

    def load(self, filepath):
        """
        Load a Word2Vec model from the specified filepath.
        :param filepath: Path to load the model from.
        """
        self.model = Word2Vec.load(filepath)

    def get_vector(self, word):
        """
        Get the vector representation of a word.
        :param word: Word to retrieve the vector for.
        :return: Vector representation of the word.
        """
        if self.model and word in self.model.wv:
            return self.model.wv[word]
        else:
            raise ValueError(f"Word '{word}' not in vocabulary or model not loaded.")
