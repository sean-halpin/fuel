import numpy

from numpy.testing import assert_raises, assert_equal, assert_allclose

from fuel.datasets import Adult
from tests import skip_if_not_available


def test_adult_all():
    skip_if_not_available(datasets=['adult.hdf5'])

    dataset = Adult(('all',), load_in_memory=False)
    handle = dataset.open()
    data, labels = dataset.get_data(handle, slice(0, 10))

    """
    assert data.dtype == 'float32'
    assert data.shape == (10, 4)
    assert labels.shape == (10, 1)
    known = numpy.array([5.1, 3.5, 1.4, 0.2])
    assert_allclose(data[0], known)
    assert labels[0][0] == 0
    assert dataset.num_examples == 150
    dataset.close(handle)
    """


def test_adult_axes():
    skip_if_not_available(datasets=['adult.hdf5'])

    dataset = Adult(('all',), load_in_memory=False)
    assert_equal(dataset.axis_labels['features'],
                 ('batch', 'feature'))


def test_adult_invalid_split():
    skip_if_not_available(datasets=['adult.hdf5'])

    assert_raises(ValueError, Adult, ('dummy',))
