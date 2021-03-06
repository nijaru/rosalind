SEQ = """TTGCATTACATCATCAGTCCCTGGGCGCGAGTAGCCGCACCATATGGGATACACTAGATGGCACTAGCTATCGCAGATATGTGATATTACTTAACAACTGCCATGGCTCCGGGAACTAGGTTACTTGGACCGCTCTGGCTGACACCAGGCCCTTTACTAGCCAGTAGCGGAACCTCTATCGATTAATTTGTCAAGTCAACGTCTCGGCAGTATTAGGGGTGCTGGGCCCCGAAGCGGGAGCCCTCGATCACTTTGGCAATCCTTATCAGGAGTTGCGTTACAGGACCATTGCATGGAGCTTTCTTATTAAGTAAATTGGACTGACCATATCTATAGGCGTAGTTTAGTCCGGCAGTACAATTCTCGTATGGCAATACCCCGGAGACGGACATCTTTAGCGCCTATGCACTATTGGGAGGCCGCCGTTAAGGGCGCACCCAGGGAGGAGCTCGCTGCGGCCGTTTGATGTAATACTCGACCCAACTATTATCACGGAGGAGGTGTTTGTACCGCAGGAGGGCAGGCCCTCCGCAGTTCATACGATCTTCCCCAGTGTCCGGCGATGGCAGGGCCCACATTCATAGTAGAGGGCGCGCATCTCCACGAGTGGCGACGTGTCCTCTGCAAACTTGGGCACAACTCAGTGCGAGTGCGGGGACGCCTGTGCCAAATGCATCTGTGCACGATTAGTCAGTCGTACGGATGTACTTATGAGCTAGAACAACAATTTATTGAGTAGAATCAGAAAAGTTGGGCTCCTCACTACGAATTCTCCTGCGTAATACCCGGCGAACGGAATGTGACCGAGTAGTCGGAAAACCCTCTTACCTAGGCTCCCCAATGCACTCATCTCTAGAAAAATAT"""


def revc(seq):
    kv = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return "".join([kv[i] for i in seq[::-1]])


print(revc(SEQ))
