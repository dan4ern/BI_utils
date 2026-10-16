import os
from helpers import bio_files, fastq

# Fastq filtering function, uses helper.fastq functions
def filter_fastq(input_fastq,
                 output_fastq,
                 gc_bounds = (0, 100),
                 length_bounds = (0, 2**32),
                 quality_threshold = 0):
    """
    Reads and parses .fastq, filters reads based on selected parameters (GC-content, length, mean quality), saves results in output .fastq file in ./filtered/ folder

    Argument:
    input_fastq: str. Path to the input .fastq file
    output_fastq: str. Path to the output .fastq file
    gc_bounds: int / float or list / tuple of two numbers. A single number sets the upper bound. Default=(0, 100)
    length_bounds: int / float or list / tuple of two numbers. A single number sets the upper bound. Default=(0, 2**32)
    quality_threshold = int / float. Default=0
    
    Creates .filtered/ folder if was not created before
    Raises exception if output file with selected name already exists
    Returns 'Filtration finished!'
    """
    reads = fastq.read_fastq(input_fastq = input_fastq)
    filtered_reads = []
    for read in reads:
        if fastq.check_gc_content(gc_bounds = gc_bounds, read_from_main = read) and fastq.check_length(length_bounds = length_bounds, read_from_main = read) and fastq.check_quality_threshold(quality_threshold = quality_threshold, read_from_main = read):
            filtered_reads.append(read)
    fastq.write_fastq(filtered_reads = filtered_reads, output_fastq = output_fastq)
    return 'Filtration finished!'

# Multiline to oneline fasta converter, uses helper.bio_files functions
def convert_multiline_fasta_to_oneline(input_fasta, output_fasta = None):
    """
    Reads and parse multiline .fasta. Converts multiline .fasta to oneline .fasta for each entity and saves it

    Argument:
    input_fasta: str. Path to the input .fasta file
    output_fasta: str or None. If None, saves to output_fasta.fasta
    
    Raises exception if output file with selected name already exists
    Returns 'Conversion finished!'
    """
    seqs = bio_files.read_fasta(input_fasta = input_fasta)
    oneline_seqs = []
    for seq_list in seqs:
        header = seq_list[0]
        sequence = ''.join(seq_list[1:])
        oneline_seqs.append([header, sequence])
    bio_files.write_fasta(fasta_one_line = oneline_seqs, output_fasta = output_fasta)
    return 'Conversion finished!'

# BLAST file parsing and filtering
def parse_blast_output(input_file, output_file):
    """
    Reads and parses BLAST .txt output, for each query extracts first hit description, sorts the descriptions
alphabetically. Saves selected hits as separate file, each hit in a separate line

    Argument:
    input_file: str. Path to the input .txt file
    output_file: str. Path to the outnput file
    
    Raises exception if output file with selected name already exists
    Returns 'BLAST parsing finished!'
    """
    blasts = bio_files.read_blast(input_file = input_file)
    hits = []
    for blast in blasts:
        description_end = blast[1].index('Name')
        first_hit = blast[2][:description_end].strip()
        hits.append(first_hit)
    hits.sort()
    bio_files.write_blast(output_file = output_file, hits = hits)
    return 'BLAST parsing finished!'