import os

# Main filtering function
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

# Read .fastq function
def read_fastq(input_fastq):
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
    read_gc = (read_from_main[1].count("G") + read_from_main[1].count("C")) / len(read_from_main[1].replace('\n', '')) * 100
    if not isinstance(gc_bounds, int) and not isinstance(gc_bounds, float):
        return read_gc >= gc_bounds[0] and read_gc <= gc_bounds[1]
    else:
        return read_gc <= gc_bounds

# Check read length
def check_length(length_bounds, read_from_main):
    read_length = len(read_from_main[1].replace('\n', ''))
    if not isinstance(length_bounds, int) and not isinstance(length_bounds, float):
        return length_bounds[0] <= read_length <= length_bounds[1]
    else:
        return read_length <= length_bounds

# Check phred33 quality
def check_quality_threshold(quality_threshold, read_from_main):
    clean_quality_string = read_from_main[3].replace('\n', '')
    length = len(clean_quality_string)
    summ_quality = 0
    for n in clean_quality_string:
        summ_quality += ord(n) - 33
    return summ_quality / length >= quality_threshold

# Write .fastq function
def write_fastq(filtered_reads, output_fastq):
    if not os.path.isdir('filtered'):
        os.mkdir('filtered')
    output_path = os.path.join("filtered", output_fastq)
    if os.path.isfile(output_path):
        raise Exception('Output_fastq already exists. Choose another name.')
    else:
        with open(output_path, mode = 'w') as output:
            for read in filtered_reads:
                output.writelines(read)