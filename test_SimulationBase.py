import pytest
from pytest_mock import MockerFixture

from SimulationBase import SimulationBase
from SimulationException import SimulationException


@pytest.fixture
def simulation_base() -> SimulationBase:
    return SimulationBase(door_count=3)


def test_get_a_random_door(mocker: MockerFixture, simulation_base: SimulationBase):
    for i in range(len(simulation_base._doors)):
        mocker.patch("random.randint", return_value=i)
        assert simulation_base._get_a_random_door() == (i, simulation_base._doors[i])


def test_get_doors_except_no_indexes(simulation_base: SimulationBase):
    assert simulation_base._get_doors_except_indexes(indexes=[]) == simulation_base._doors


def test_get_doors_except_one_indexes(simulation_base: SimulationBase):
    for i in range(len(simulation_base._doors)):
        assert simulation_base._get_doors_except_indexes(indexes=[i]) == [
            simulation_object for j, simulation_object in enumerate(simulation_base._doors) if j != i
        ]


def test_get_a_random_door_except_indexes(mocker: MockerFixture, simulation_base: SimulationBase):
    for i in range(len(simulation_base._doors)):
        mocker.patch("random.randint", return_value=i)
        assert simulation_base._get_a_random_door_except_indexes(indexes=[]) == (i, simulation_base._doors[i])


def test_get_a_random_door_no_result(mocker: MockerFixture, simulation_base: SimulationBase):
    with pytest.raises(SimulationException):
        assert simulation_base._get_a_random_door_except_indexes(
            indexes=[i for i in range(len(simulation_base._doors))])
