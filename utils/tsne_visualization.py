import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def plot_tsne_embeddings(embeddings, words, output_path):
    """
    Plot t-SNE visualization of word embeddings.
    
    :param embeddings: List of word vectors.
    :param words: List of words corresponding to the embeddings.
    :param output_path: Path to save the t-SNE plot.
    """
    tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
    reduced_embeddings = tsne.fit_transform(embeddings)
    
    plt.figure(figsize=(12, 12))
    for i, label in enumerate(words):
        x, y = reduced_embeddings[i]
        plt.scatter(x, y)
        plt.annotate(label, (x, y), fontsize=9, alpha=0.7)
    
    plt.title("t-SNE Visualization of Word Embeddings")
    plt.savefig(output_path)
    plt.close()
