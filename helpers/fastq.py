import os

# Read .fastq function
def read_fastq(input_fastq):
    """
    Helper function for filter_fastq() function
    Reads and parses .fastq

    Argument:
    input_fastq: str. Path to the input .fastq file

    Returns list of lists
    """
    with open(input_fastq) as inp_fastq:
        reads = []
        for read_data in inp_fastq:
            read_seq = inp_fastq.readline()
            read_comment = inp_fastq.readline()
            read_quality = inp_fastq.readline()
            read = [read_data, read_seq, read_comment, read_quality]
            reads.append(read)
        return reads

# Check GC content function
def check_gc_content(gc_bounds, read_from_main):
    """
    Helper function for filter_fastq() function
    Checks if GC-content of read is within acceptable bounds

    Argument:
    gc_bounds: int / float or list / tuple of two numbers. A single number sets the upper bound
    read_from_main: list

    Returns bool
    """
    clean_seq = read_from_main[1].replace('\n', '').upper()
    read_gc = (clean_seq.count("G") + clean_seq.count("C")) / len(clean_seq) * 100
    if not isinstance(gc_bounds, int) and not isinstance(gc_bounds, float):
        return read_gc >= gc_bounds[0] and read_gc <= gc_bounds[1]
    else:
        return read_gc <= gc_bounds

# Check read length
def check_length(length_bounds, read_from_main):
    """
    Helper function for filter_fastq() function
    Checks if read length is within acceptable bounds

    Argument:
    length_bounds: int / float or list / tuple of two numbers. A single number sets the upper bound
    read_from_main: list

    Returns bool
    """
    read_length = len(read_from_main[1].replace('\n', ''))
    if not isinstance(length_bounds, int) and not isinstance(length_bounds, float):
        return length_bounds[0] <= read_length <= length_bounds[1]
    else:
        return read_length <= length_bounds

# Check phred33 quality
def check_quality_threshold(quality_threshold, read_from_main):
    """
    Helper function for filter_fastq() function
    Checks if mean read phred33 quality is greater than or equal to selected threshold

    Argument:
    quality_threshold: int / float
    read_from_main: list

    Returns bool
    """
    clean_quality_string = read_from_main[3].replace('\n', '')
    length = len(clean_quality_string)
    summ_quality = 0
    for n in clean_quality_string:
        summ_quality += ord(n) - 33
    return summ_quality / length >= quality_threshold

# Write .fastq function
def write_fastq(filtered_reads, output_fastq):
    """
    Helper function for filter_fastq() function
    Saves results of .fastq filtering to .fastq file in ./filtered/ folder

    Arguments:
    filtered_reads: list of lists
    output_fastq: str. Output filename in ./filtered/ folder

    Creates .filtered/ folder if was not created before
    Raises exception if output file with selected name already exists
    """
    if not os.path.isdir('filtered'):
        os.mkdir('filtered')
    output_path = os.path.join("filtered", output_fastq)
    if os.path.isfile(output_path):
        raise Exception('Output file with this name already exists. Choose another name.')
    else:
        with open(output_path, mode = 'w') as output:
            for read in filtered_reads:
                output.writelines(read)