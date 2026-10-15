import os

# Read fasta function
def read_fasta(input_fasta):
    with open('example_multiline_fasta.fasta') as inp_fasta:
        seqs = []
        seq = []
        for line in inp_fasta:
            if not line.startswith('>'):
                seq.append(line.replace('\n', ''))
            else:
                if seq:
                    seqs.append(seq)
                seq = []
                seq.append(line.replace('\n', ''))
        if seq:
            seqs.append(seq)