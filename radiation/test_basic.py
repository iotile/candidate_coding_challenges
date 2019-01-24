import pytest
import os
from iotile.core.hw.hwmanager import HardwareManager

from iotile.core.dev.registry import ComponentRegistry

@pytest.fixture
def registry():
    reg = ComponentRegistry()
    reg.clear()
    reg.clear_components()
    reg.add_component(os.getcwd())

    yield reg

@pytest.fixture
def con():
    hw = HardwareManager(port='virtual:./radiation_device.py')
    hw.connect_direct(1)
    con = hw.controller()
    yield con

    hw.disconnect()


def test_zero_readings(registry, con):
    assert con.get_average() == 0
    assert con.get_min_max() == (0, 0)
    assert con.get_median() == 0
    assert con.get_mode() == 0

def test_one_reading(registry, con):
    con.add_radiation_reading(1)
    assert con.get_average() == 1
    assert con.get_min_max() == (1, 1)
    assert con.get_median() == 1
    assert con.get_mode() == 0

def test_two_readings(registry, con):
    con.add_radiation_reading(1)
    con.add_radiation_reading(2)
    assert con.get_average() == 1.5
    assert con.get_min_max() == (1, 2)
    assert con.get_median() == 1.5
    assert con.get_mode() == 0

def test_three_readings(registry, con):
    con.add_radiation_reading(1)
    con.add_radiation_reading(2)
    con.add_radiation_reading(3)
    assert con.get_average() == 2
    assert con.get_min_max() == (1, 3)
    assert con.get_median() == 2
    assert con.get_mode() == 0

def test_four_readings(registry, con):
    con.add_radiation_reading(1)
    con.add_radiation_reading(1)
    con.add_radiation_reading(3)
    con.add_radiation_reading(3)
    assert con.get_average() == 2
    assert con.get_min_max() == (1, 3)
    assert con.get_median() == 2
    assert con.get_mode() == 1