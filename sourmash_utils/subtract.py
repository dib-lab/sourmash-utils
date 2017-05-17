#! /usr/bin/env python
from __future__ import print_function
import sys
import sourmash_lib.signature


def subtract(infile=None, filenames=None):
    print('loading', infile)
    with open(infile) as f:
        sigs = list(sourmash_lib.signature.load_signatures(f))
    assert len(sigs) == 1
    sig = sigs[0]

    mins = set(sig.minhash.get_mins())
    orig_mins = set(mins)

    for filename in filenames:
        print('subtracting', filename)
        with open(filename, 'r') as f:
            sigs = list(sourmash_lib.signature.load_signatures(f))
        assert len(sigs) == 1
        submins = sigs[0].minhash.get_mins()
        submins = set(submins)

        mins = mins - submins

    print('started with {} hashes, ended with {}'.format(len(orig_mins),
                                                         len(mins)))

    new_minhash = sig.minhash.copy_and_clear()
    new_minhash.add_many(mins)
    sig.minhash = new_minhash

    with open(infile + '.sub', 'wt') as out_fp:
        print(sourmash_lib.signature.save_signatures([sig]),
              file=out_fp)


def main(args=None):
    if args is None:
        infile = sys.argv[1]
        filenames = sys.argv[2:]
    else:
        infile = args[0]
        filenames = args[1:]

    subtract(infile, filenames)

    return 0
