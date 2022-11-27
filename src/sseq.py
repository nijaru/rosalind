from rosalib import parse_fasta_values


def sseq(fasta):
    values = parse_fasta_values(fasta)
    seq = values[0]
    sseq = values[1]

    i = 0
    idxs = []
    for c in sseq:
        idxs.append(seq[i:].index(c) + i + 1)
        i = idxs[-1]

    return " ".join([str(x) for x in idxs])


def main():
    # fasta = ">Rosalind_14\nACGTACGTGACG\n>Rosalind_18\nGTA"
    with open("../data/rosalind_sseq.txt") as fasta:
        print(sseq(fasta.read().strip()))


if __name__ == "__main__":
    main()
