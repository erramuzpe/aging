from __future__ import absolute_import, division, print_function
import os.path as op
# import numpy as np
# import numpy.testing as npt

import aging as ag
# import aging.proc as pr

data_path = op.join(ag.__path__[0], 'data')


def test_transform_data():
    """
    Testing the transformation of the data from raw data to functions
    used for fitting a function.

    """
    # We start with actual data. We test here just that reading the data in
    # different ways ultimately generates the same arrays.
    pass

