import os

# Read fasta function
def read_fasta(input_fasta):
    with open(input_fasta) as inp_fasta:
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
    return seqs

# Write oneline fasta
def write_fasta(fasta_one_line, output_fasta = None):
    if output_fasta == None:
        output_fasta = './output_fasta.fasta'
    if os.path.isfile(output_fasta):
        raise Exception('Output fasta file with this name already exists. Choose another name.')
    else:
        with open(output_fasta, mode = 'w') as output:
            for seq in fasta_one_line:
                output.write(seq[0] + '\n')
                output.write(seq[1] + '\n')