import time
from tqdm import tqdm


def fbi_hacking():
    print("FBI Hacking")

    for i in tqdm(range(100)):
        time.sleep(0.5)

    print("Hacking Complete")


if __name__ == "__main__":
    fbi_hacking()

