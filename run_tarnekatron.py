from tarnekatron import Tarnekatron

if __name__ == "__main__":
    tarnekatron = Tarnekatron(weights_path="nt-all.hdf5")

    print(tarnekatron.generate(10))
