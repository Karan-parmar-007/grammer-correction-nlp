from textblob import TextBlob
from gramformer import Gramformer

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = Gramformer(models=1)  # Initialize gramformer
    
    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        # Correct grammar using gramformer
        corrected_sentences = list(self.grammar_check.correct(text, max_candidates=1))
        foundmistakes_count = len(corrected_sentences) - 1  # Number of grammar corrections
        return corrected_sentences[0], foundmistakes_count