from textgenrnn import textgenrnn

class Tarnekatron:
    def __init__(self):
        self.textgen = textgenrnn()


    def generate(self):
        return self.textgen.generate()
