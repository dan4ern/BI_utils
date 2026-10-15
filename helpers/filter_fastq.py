import os

# Main filtering function
def filter_fastq(input_fastq, output_fastq, gc_bounds = (0, 100), length_bounds = (0, 2**32), quality_threshold = 0):
    pass

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
def check_gc_content(gc_bound, read_from_main):
    read_gc = (read_from_main[1].count("G") + read_from_main[1].count("C")) / len(read_from_main[1].replace('\n', '')) * 100
    if not isinstance(gc_bound, int) and not isinstance(gc_bound, float):
        return read_gc >= gc_bound[0] and read_gc <= gc_bound[1]
    else:
        return read_gc <= gc_bound

# Check read length
def check_length(length_bounds, read_from_main):
    read_length = len(read_from_main[1].replace('\n', ''))
    if not isinstance(length_bounds, int) and not isinstance(length_bounds, float):
        return length_bounds[0] <= read_length <= length_bounds[1]
    else:
        return read_length <= length_bounds

# Check phred33 quality
def check_quality_threshold(read_from_main, quality_threshold):
    length = len(read_from_main[3])
    summ_quality = 0
    for n in read_from_main[3]:
        summ_quality += ord(n) - 33
    return summ_quality / length >= quality_threshold