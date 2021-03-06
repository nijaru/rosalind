import itertools


def parse_fasta(fasta):
    return zip(*parse_fasta_dict(fasta).items())


def parse_fasta_keys(fasta):
    return list(parse_fasta_dict(fasta).keys())


def parse_fasta_values(fasta):
    return list(parse_fasta_dict(fasta).values())

""">Sample_id
ACGTACGTACGTACGTACGTACGTACGTACGT

>Sample_id
ACGTACGTACGTACGTACGTACGTACGTACGT

>Sample_id
ACGTACGTACGTACGTACGTACGTACGTACGT

>Sample_id
ACGTACGTACGTACGTACGTACGTACGTACGT

>Sample_id
ACGTACGTACGTACGTACGTACGTACGTACGT

>Sample_id
ACGTACGTACGTACGTACGTACGTACGTACGT
"""


def parse_fasta_dict(fasta):
    # format into lines [1,2...] where 1 is sample id and 2 is sample
    fasta = fasta.strip().split(">")[1:]
    fasta = [x.strip().split("\n") for x in fasta]
    fasta = list(itertools.chain.from_iterable(fasta))
    fasta = [x.replace("\n", "") for x in fasta]

    # create dict {sample_id: sample}
    pairs = {fasta[i]: fasta[i + 1] for i in range(0, len(fasta), 2)}
    return pairs
