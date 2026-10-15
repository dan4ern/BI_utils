import os
from helpers import bio_files, fastq

# Fastq filtering function
def filter_fastq(input_fastq,
                 output_fastq,
                 gc_bounds = (0, 100),
                 length_bounds = (0, 2**32),
                 quality_threshold = 0):
    reads = read_fastq(input_fastq = input_fastq)
    filtered_reads = []
    for read in reads:
        if check_gc_content(gc_bounds = gc_bounds, read_from_main = read) and check_length(length_bounds = length_bounds, read_from_main = read) and check_quality_threshold(quality_threshold = quality_threshold, read_from_main = read):
            filtered_reads.append(read)
    write_fastq(filtered_reads = filtered_reads, output_fastq = output_fastq)
    return 'Filtration finished!'


# Multiline to oneline fasta converter
def convert_multiline_fasta_to_oneline(input_fasta, output_fasta = None):
    seqs = read_fasta(input_fasta = input_fasta)
    oneline_seqs = []
    for seq_list in seqs:
        header = seq_list[0]
        sequence = ''.join(seq_list[1:])
        oneline_seqs.append([header, sequence])
    write_fasta(fasta_one_line = oneline_seqs, output_fasta = output_fasta)
    return 'Conversion finished!'