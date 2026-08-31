from collections import defaultdict

def word_count_dict(sentences: list) -> dict:
    tokens = defaultdict(int)
    
    for sentence in sentences:
        for word in sentence:
            tokens[word] += 1

    return tokens
    
    