from tarnekatron import Tarnekatron

prefix = "nt-all"

if __name__ == "__main__":
    tarnekatron = Tarnekatron()
    tarnekatron.train("{}.txt".format(prefix))
    tarnekatron.save("{}.hdf5".format(prefix))
