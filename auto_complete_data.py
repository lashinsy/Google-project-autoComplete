class AutoCompleteData:

    def __init__(self, sentence, source_text, offset, score=0):
        self.completed_sentence = sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score
