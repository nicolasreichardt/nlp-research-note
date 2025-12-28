from collections import Counter
import matplotlib.pyplot as plt

def get_word_frequencies(tokens, stop_words=None, min_length=2):
    """
    Count word frequencies from a list of tokens.
    
    :param tokens: List of tokens.
    :param stop_words: List of stopwords to exclude.
    :param min_length: Minimum word length to include.
    :return: Counter object with word frequencies.
    """
    if stop_words is None:
        stop_words = []
    
    filtered_tokens = [token.lower() for token in tokens 
                       if token.lower() not in stop_words and len(token) > min_length]
    return Counter(filtered_tokens)


def plot_word_frequency_comparison(freq1, freq2, label1, label2, top_n=20, output_path=None):
    """
    Create side-by-side horizontal bar charts comparing word frequencies.
    
    :param freq1: Counter object for first document.
    :param freq2: Counter object for second document.
    :param label1: Label for first document.
    :param label2: Label for second document.
    :param top_n: Number of top words to display.
    :param output_path: Path to save the plot (optional).
    """
    top1 = freq1.most_common(top_n)
    top2 = freq2.most_common(top_n)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    
    # First document
    words1, counts1 = zip(*top1)
    axes[0].barh(range(len(words1)), counts1, color='#1f77b4')
    axes[0].set_yticks(range(len(words1)))
    axes[0].set_yticklabels(words1)
    axes[0].invert_yaxis()
    axes[0].set_xlabel('Frequency')
    axes[0].set_title(f'{label1} - Top {top_n} Words')
    
    # Second document
    words2, counts2 = zip(*top2)
    axes[1].barh(range(len(words2)), counts2, color='#ff7f0e')
    axes[1].set_yticks(range(len(words2)))
    axes[1].set_yticklabels(words2)
    axes[1].invert_yaxis()
    axes[1].set_xlabel('Frequency')
    axes[1].set_title(f'{label2} - Top {top_n} Words')
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
    
    plt.show()
