from textgenrnn import textgenrnn

class Tarnekatron:
    def __init__(self):
        self.textgen = textgenrnn()


    def generate(self, lines=1):
        return self.textgen.generate(lines)
