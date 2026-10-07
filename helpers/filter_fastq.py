import os

def filter_fastq(input_fastq, output_fastq, gc_bounds = (0, 100), length_bounds = (0, 2**32), quality_threshold = 0):
    pass

def read_fastq(input_fastq):
    with open(input_fastq) as inp_fastq:
        reads = []
        for line in inp_fastq:
            if line.startswith('@'):
                read = []
                read.append(line)
            else:
                read.append(line)
            reads.append(read)
        return reads

def check_gc_content(gc_bound, read_from_main):
    read_gc = (read_from_main[1].count("G") + read_from_main[1].count("C")) / len(read_from_main[1].replace('\n', '')) * 100
    if not isinstance(gc_bound, int):
        if read_gc >= gc_bound[0] and read_gc <= gc_bound[1]:
            return True
        return False
    else:
        if read_gc <= gc_bound:
            return True
        return False