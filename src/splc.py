from prot import prot
from rna import rna
from rosalib import parse_fasta_values


def splc(fasta):
    values = parse_fasta_values(fasta)
    seq = values[0]
    for x in values[1:]:
        seq = seq.replace(x, "")
    return prot(rna(seq))


def main():
    fasta = ">Rosalind_10\nATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG\n>Rosalind_12\nATCGGTCGAA\n>Rosalind_15\nATCGGTCGAGCGTGT"
    # fasta = open("/home/nick/Downloads/rosalind_splc.txt").read()
    print(splc(fasta))


if __name__ == "__main__":
    main()
