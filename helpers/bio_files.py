import os

# Read fasta function
def read_fasta(input_fasta):
    """
    Helper function for convert_multiline_fasta_to_oneline() function
    Reads and parses .fasta

    Argument:
    input_fasta: str. Path to the input .fasta file

    Returns list of lists
    """
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
    """
    Helper function for convert_multiline_fasta_to_oneline() function
    Saves results of input .fasta conversion in .fasta format

    Arguments:
    fasta_one_line: list of lists
    output_fasta: str. Path to the output .fasta file. Optional, if not chosen - "output_fasta.fasta" is used

    Raises exception if output file with selected name already exists
    """
    if output_fasta == None:
        output_fasta = './output_fasta.fasta'
    if os.path.isfile(output_fasta):
        raise Exception('Output fasta file with this name already exists. Choose another name.')
    else:
        with open(output_fasta, mode = 'w') as output:
            for seq in fasta_one_line:
                output.write(seq[0] + '\n')
                output.write(seq[1] + '\n')

# Read blast.txt file
def read_blast(input_file):
    """
    Helper function for parse_blast_output() function
    Reads and parses .txt blast results

    Argument:
    input_file: str. Path to the input .txt file

    Returns list of lists
    """
    blasts = []
    with open(input_file) as inp_blast:
        for line in inp_blast:
            if line.startswith('Query #'):
                for _ in range(3):
                    inp_blast.readline()
                columns = inp_blast.readline()
                first_blast = inp_blast.readline()
                blasts.append([line, columns, first_blast])
    return blasts

# Write blast filtering/parsing output
def write_blast(output_file, hits):
    """
    Helper function for parse_blast_output() function
    Saves results of BLAST filtering/parsing to file, each selected hit of BLAST as separate line

    Arguments:
    output_file: str. Path to the output file
    hits: list

    Raises exception if output file with selected name already exists
    """
    if os.path.isfile(output_file):
        raise Exception('Output file with this name already exists. Choose another name.')
    with open(output_file, mode = 'w') as out_blast:
        for hit in hits:
            out_blast.write(hit + '\n')