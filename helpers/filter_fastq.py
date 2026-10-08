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