def rna(seq):
    return seq.replace("T", "U")


def main():
    print(rna("AAAACCCGGT"))


if __name__ == "__main__":
    main()
