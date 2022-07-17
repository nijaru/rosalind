from rosalib import parse_fasta_values


def sseq(fasta):
    values = parse_fasta_values(fasta)
    seq = values[0]
    sseq = values[1]

    ret = []
    i = 0
    for c in sseq:

    return " ".join(ret)

    # for i in [i for i, x in enumerate(seq) if x == sseq[0]]:
    #     for j in range(1, len(sseq)):
    #         if sseq[j] in seq[i:]:
    #             if j + 1 == len(sseq):
    #                 if ret == []:
    #                     ret.append(i + 1)
    #                 else:
    #                     ret.append(i + 2)


def main():
    fasta = ">Rosalind_14\nACGTACGTGACG\n>Rosalind_18\nGTA"
    # fasta = open("/home/nick/Downloads/rosalind_sseq.txt").read().strip()
    print(sseq(fasta))


if __name__ == "__main__":
    main()
