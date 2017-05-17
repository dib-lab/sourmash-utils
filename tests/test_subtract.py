#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sourmash_utils
----------------------------------

Tests for `sourmash_utils` module.
"""

import os

import sourmash_lib.signature
import sourmash_lib.tests.sourmash_tst_utils as utils


def test_subtract_from_sourmash():
    with utils.TempDirectory() as location:
        testdata1 = utils.get_test_data('short.fa')
        testdata2 = utils.get_test_data('short2.fa')

        status, out, err = utils.runscript('sourmash',
                                           ['compute', testdata1, testdata2],
                                           in_directory=location)

        with open(os.path.join(location, 'short.fa.sig')) as f:
            sigs = list(sourmash_lib.signature.load_signatures(f))
            s1mins = set(sigs[0].minhash.get_mins())

        with open(os.path.join(location, 'short2.fa.sig')) as f:
            sigs = list(sourmash_lib.signature.load_signatures(f))
            s2mins = set(sigs[0].minhash.get_mins())

        status, out, err = utils.runscript('sourmash',
                                           ['utils', 'subtract',
                                            'short.fa.sig', 'short2.fa.sig'],
                                           in_directory=location)
        print(out)
        assert os.path.exists(os.path.join(location, 'short.fa.sig.sub'))

        with open(os.path.join(location, 'short.fa.sig.sub')) as f:
            sigs = list(sourmash_lib.signature.load_signatures(f))
            submins = set(sigs[0].minhash.get_mins())

        assert submins == s1mins - s2mins


def test_subtract_from_sourmash_utils():
    with utils.TempDirectory() as location:
        testdata1 = utils.get_test_data('short.fa')
        testdata2 = utils.get_test_data('short2.fa')

        status, out, err = utils.runscript('sourmash',
                                           ['compute', testdata1, testdata2],
                                           in_directory=location)

        with open(os.path.join(location, 'short.fa.sig')) as f:
            sigs = list(sourmash_lib.signature.load_signatures(f))
            s1mins = set(sigs[0].minhash.get_mins())

        with open(os.path.join(location, 'short2.fa.sig')) as f:
            sigs = list(sourmash_lib.signature.load_signatures(f))
            s2mins = set(sigs[0].minhash.get_mins())

        status, out, err = utils.runscript('sourmash-utils',
                                           ['subtract',
                                            'short.fa.sig', 'short2.fa.sig'],
                                           in_directory=location,
                                           distribution='sourmash_utils')
        print(out)
        assert os.path.exists(os.path.join(location, 'short.fa.sig.sub'))

        with open(os.path.join(location, 'short.fa.sig.sub')) as f:
            sigs = list(sourmash_lib.signature.load_signatures(f))
            submins = set(sigs[0].minhash.get_mins())

        assert submins == s1mins - s2mins
