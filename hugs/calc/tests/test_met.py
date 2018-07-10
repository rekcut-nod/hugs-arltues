"""Test the `met` module."""

from hugs.calc import get_wind_dir, get_wind_speed, get_wind_components

import numpy as np
from numpy.testing import assert_almost_equal, assert_array_almost_equal
import pytest


def test_speed():
    """Test calculating wind speed."""
    u = np.array([4., 2.,0., 0.])
    v = np.array([0., 2., 4., 0.])

    speed = get_wind_speed(u, v)

    s2 = np.sqrt(2.)
    true_speed = np.array([4., 2 * s2, 4., 0.])

    assert_array_almost_equal(true_speed, speed, 4)


def test_scalar_speed():
    """Test wind speed with scalars."""
    s = get_wind_speed(-3., -4.)
    assert_almost_equal(s, 5., 3)


def test_dir():
    """Test calculating wind direction."""
    u = np.array([4., 2., 0., 0.])
    v = np.array([0., 2., 4., 0.])

    direc = get_wind_dir(u, v)

    true_dir = np.array([270., 225., 180., 270.])

    assert_array_almost_equal(true_dir, direc, 4)

def test_get_wind_components():
    """Test that get_wind_components works with scalar and array inputs"""
    u,v = get_wind_components(50, 0)
    assert_almost_equal(u, 0, 3)
    assert_almost_equal(v, -50, 3)

    directions = np.array([0, 45, 90, 135, 180, 225, 270, 315, 360])
    speeds = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])

    sq2 = np.sqrt(2.0)

    u, v = get_wind_components(speeds, directions)

    expected_U = np.array([0, -1.0/sq2, -1.0, -1.0/sq2, 0, 1.0/sq2, 1.0, 1.0/sq2, 0])
    expected_V = np.array([-1.0, -1.0/sq2, 0.0, 1.0/sq2, 1.0, 1.0/sq2, 0.0, -1.0/sq2, -1.0])

    assert_array_almost_equal(expected_U, u, 4)
    assert_array_almost_equal(expected_V, v, 4)

def test_warning_direction():
    """Test that warning is raised wind direction > 360."""
    with pytest.warns(UserWarning):#warnings.warn give UserWarning by default
        get_wind_components(3, 480)

