from tarnekatron import Tarnekatron

if __name__ == "__main__":
    tarnekatron = Tarnekatron()
    tarnekatron.train("talib-kweli.txt")
    tarnekatron.save()
