import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        # self.id_last = 4
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        self.word_to_id[self.pad_token] = 0
        self.word_to_id[self.unk_token] = 1
        self.word_to_id[self.bos_token] = 2
        self.word_to_id[self.eos_token] = 3
    
        self.id_to_word[0] = self.pad_token
        self.id_to_word[1] = self.unk_token
        self.id_to_word[2] = self.bos_token
        self.id_to_word[3] = self.eos_token

        self.vocab_size = 4
        
        for lines in texts:
            for text in lines.split():
                if text not in self.word_to_id:
                    self.word_to_id[text] = self.vocab_size
                    self.id_to_word[self.vocab_size ] = text
                    self.vocab_size  +=1

    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # tokens = [self.word_to_id[self.bos_token]]
        tokens = []
        for word in text.split():
            tokens.append(self.word_to_id.get(word, self.word_to_id[self.unk_token]))
            # tokens.append(self.word_to_id[self.pad_token])
        # tokens[-1] = self.word_to_id[self.eos_token]
        # tokens.append(self.word_to_id[self.eos_token])

        return tokens
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        words = []
        for id in ids:
            words.append(self.id_to_word[id])

        return " ".join(words)
