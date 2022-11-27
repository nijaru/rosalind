def parse_fasta_dict(fasta):
    fasta = fasta.strip()
    fasta = fasta.replace(">", "", 1).split(">")
    fasta = [x.split("\n", 1) for x in fasta]
    fasta = {pair[0]: pair[1].replace("\n", "") for pair in fasta}
    return fasta


def parse_fasta(fasta):
    return zip(*parse_fasta_dict(fasta).items())


def parse_fasta_keys(fasta):
    return list(parse_fasta_dict(fasta).keys())


def parse_fasta_values(fasta):
    return list(parse_fasta_dict(fasta).values())
