from autocorrect import Speller

def correct_spelling(sequence):
    spell = Speller()
    words = sequence.split()
    corrected_sequence = []

    for word in words:
        corrected_word = spell(word)
        corrected_sequence.append(corrected_word)

    return ' '.join(corrected_sequence)
