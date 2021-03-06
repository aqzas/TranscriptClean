import pytest
from pyfasta import Fasta
import sys
sys.path.append("..")
import spliceJunction as sj
import intronBound as ib
import TranscriptClean as TC
import dstruct as dstruct
@pytest.mark.unit

class TestFindClosestSJ(object):

    def test_find_closest_sj_plus(self):

        # Process reference junctions
        sjFile = "input_files/test_junctions.txt"
        tmp_dir = "scratch/test/TC_tmp/"
        chroms = set(["chr1"])
        donors, acceptors, sjDict = TC.processSpliceAnnotation(sjFile, tmp_dir,
                                                               chroms)

        # Intron bound info
        transcriptID = "test_read"
        jnNumber = 0
        chrom = "chr1"
        start = 23071350
        end = 23072124
        strand = "+"
        genome = Fasta("input_files/hg38_chr1.fa")

        junction = sj.SpliceJunction(transcriptID, jnNumber, chrom,
                                     start, end, strand, genome, sjDict)

        closest_donor, closest_acceptor = TC.find_closest_ref_junction(junction, donors, acceptors)
        assert closest_donor.end == 23071360
        assert closest_acceptor.end == 23072123
        
         
