#-------------------------------------------------------------------------------
#
#   MEvoLib  Copyright (C) 2016  J. Alvarez-Jarreta
#
#   This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#   This is free software, and you are welcome to redistribute it under certain
#   conditions; type `show c' for details.
#
#-------------------------------------------------------------------------------
# File :  test_Cluster_NaiveRows.py
# Last version :  v1.00 ( 16/Jul/2016 )
# Description :  Test suite for MEvoLib.Cluster module: Naive Rows software
#       tool.
#-------------------------------------------------------------------------------
# Historical report :
#
#   DATE :  16/Jul/2016
#   VERSION :  v1.00
#   AUTHOR(s) :  J. Alvarez-Jarreta
#
#-------------------------------------------------------------------------------

import os
import unittest

from Bio import SeqIO

from MEvoLib import Cluster
from MEvoLib._py3k import viewvalues


#-------------------------------------------------------------------------------

# Try to avoid problems when the OS is in another language
os.environ['LANG'] = 'C'


#-------------------------------------------------------------------------------

class ClusterTestCase ( unittest.TestCase ) :

    def setUp ( self ) :
        self.files_to_clean = set()


    def tearDown ( self ) :
        for filename in self.files_to_clean :
            if ( os.path.isfile(filename) ) :
                os.remove(filename)


    def add_file_to_clean ( self, filename ) :
        """
        Adds a file for deferred removal by the tearDown() routine.

        Arguments :
            filename  ( string )
                File name to remove by the tearDown() routine.
        """
        self.files_to_clean.add(filename)



class NaiveRowsTestCase ( ClusterTestCase ) :

    def test_clustering ( self ) :
        """
        Testing procedure for the naive rows method.
        """
        infile = 'Fasta/f001.fasta'
        informat = 'fasta'
        # Check the input
        self.assertTrue(os.path.isfile(infile))
        self.assertEqual(len(list(SeqIO.parse(infile, informat))), 50)
        # Generate the alignment
        subset_dict = Cluster.get_subsets('rows', infile, informat, 5)
        # Check the output
        self.assertEqual(len(subset_dict), 5)
        for subset in viewvalues(subset_dict) :
            self.assertEqual(len(subset), 10)


#-------------------------------------------------------------------------------

if ( __name__ == '__main__' ) :
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)


#-------------------------------------------------------------------------------
