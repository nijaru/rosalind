import itertools


def parse_fasta(fasta):
    return zip(*parse_fasta_dict(fasta).items())


def parse_fasta_dict(fasta):
    # format into lines [1,2...] where 1 is sample id and 2 is sample
    fasta = fasta.strip().split(">")[1:]
    fasta = [x.split("\n", 1) for x in fasta]
    fasta = list(itertools.chain.from_iterable(fasta))
    fasta = [x.replace("\n", "") for x in fasta]

    # create dict {sample_id: sample}
    pairs = {fasta[i]: fasta[i + 1] for i in range(0, len(fasta), 2)}
    return pairs
