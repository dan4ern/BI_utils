# BI_utils

Python utilities for filtering .FASTQ reads by GC-content, length and phred33 quality, converting multiline .FASTA files to oneline and parsing BLAST results.

## Requirements and setup

Only the Python standard library is used.

Download or clone this repository to use it. Keep `BI_utils.py` and the `helpers/` folder together.

## Usage

```python
import BI_utils
```

### Filter .FASTQ reads

```python
BI_utils.filter_fastq(
    input_fastq="input.fastq",
    output_fastq="filtered.fastq",
    gc_bounds=(45, 80),
    length_bounds=(10, 100),
    quality_threshold=20,
)
```

```python
BI_utils.filter_fastq(
    input_fastq="input.fastq",
    output_fastq="filtered.fastq",
    gc_bounds=80,
    length_bounds=100,
    quality_threshold=20,
)
```

Reads must pass all three filters. The result is saved to `./filtered/passed.fastq`; the folder is created if needed.

Parameters description:
- `gc_bounds` - GC-content bounds, in percent. Default - `(0, 100)`
- `length_bounds` - Read length bounds, in nucleotides. Default - `(0, 2**32)`
- `quality_threshold` - Minimum mean quality for all bases, using phred33. Default - `0`

GC and length bounds can be a list or tuple of two numbers, or a single number, which used as upper bound. All boundaries are inclusive.

### Convert multiline .FASTA

```python
BI_utils.convert_multiline_fasta_to_oneline(
    input_fasta="input.fasta", output_fasta="oneline_output.fasta"
)
```

For aach header, its sequence is joined into oneline format. If `output_fasta` is absent or `None`, the result is saved to default `output_fasta.fasta`.

### Parse BLAST results

```python
BI_utils.parse_blast_output(
    input_file="blast_results.txt", output_file="first_hits.txt"
)
```

For each query in BLAST results, extracts the first hit description, sorts it alphabetically and saves. Each hit as separate line.

The parser th input file format as used in `example_blast_results.txt`.

## Notes

- FASTQ and FASTA full records are saved in memory
- Existing output files are not overwritten
