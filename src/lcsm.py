from rosalib import parse_fasta_values

FASTA = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""


def lcsm(fasta):
    values = parse_fasta_values(fasta)
    sub = ""
    if len(values) > 1 and len(values[0]) > 0:
        for i in range(len(values[0])):
            for j in range(len(values[0]) - i + 1):
                if j > len(sub) and all(
                    values[0][i : i + j] in x for x in values
                ):
                    sub = values[0][i : i + j]
    return sub


print(lcsm(FASTA))
