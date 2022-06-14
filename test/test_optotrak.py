from pathlib import Path

from numpy.testing import assert_array_equal

from optotrak import load_optotrak

TESTROOT = Path(__file__).parent


def test_load_optotrak():
    data = load_optotrak(TESTROOT / 'test_optotrak.tsv', delimiter='\t')
    assert_array_equal(data.loc[24, 'Column4'],
                       [72.362426758, -320.086181641, -2410.855712891])
    assert data.attrs['Count'] == 500
    assert data.attrs['Frequency'] == 50.0
    assert data.attrs['Units'] == 'mm'
