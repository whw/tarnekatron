from textgenrnn import textgenrnn

class Tarnekatron:
    def __init__(self, weights_path=None):
        if weights_path is not None:
            print("Loading previously trained weights")
            self.textgen = textgenrnn(weights_path=weights_path)
        else:
            print("Creating intital model")
            self.textgen = textgenrnn()


    def train(self, file_path):
        self.textgen.train_from_file(file_path)

    def save(self, weights_path="weights.hdf5"):
        self.textgen.save(weights_path=weights_path)

    def generate(self, lines=1):
        return self.textgen.generate(lines)
