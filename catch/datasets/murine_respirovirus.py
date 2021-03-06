"""Dataset with 'Murine respirovirus' sequences.

A dataset with 22 'Murine respirovirus' genomes.

THIS PYTHON FILE WAS GENERATED BY A COMPUTER PROGRAM! DO NOT EDIT!
"""

import sys

from catch.datasets import GenomesDatasetSingleChrom


ds = GenomesDatasetSingleChrom(__name__, __file__, __spec__)
ds.add_fasta_path("data/murine_respirovirus.fasta.gz", relative=True)
sys.modules[__name__] = ds
