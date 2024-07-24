from collections import Counter
import re

def count_words_in_file(filename):
    
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    
    words = re.findall(r'\b\w+\b', text)
    
    word_counts = Counter(words)
    
    sorted_word_counts = dict(sorted(word_counts.items()))
    
    for word, count in sorted_word_counts.items():
        print(f'{word}: {count}')

count_words_in_file('C:/Users/ANIL/Desktop/cognifyz python/Level2tasks/simple.txt')
count_words_in_file('C:/Users/ANIL/Desktop/cognifyz python/Level2tasks/anil.txt')
