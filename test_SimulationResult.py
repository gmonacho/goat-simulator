import pytest

from SimulationException import BadSample
from SimulationModel import ESimulationType, ESimulationObject
from SimulationResult import SimulationResult


@pytest.fixture
def simulation_result() -> SimulationResult:
    return SimulationResult()


def test_add_one_point_to_simulation_combination(simulation_result):
    for simulation_type in ESimulationType:
        for simulation_object in ESimulationObject:
            simulation_result.add_one_point_to_simulation_combination(simulation_type.value, simulation_object.value)
            assert simulation_result.get_score_specific_to_combination(simulation_type.value,
                                                                       simulation_object.value) == 1


def test_str_magic_method(simulation_result):
    with pytest.raises(BadSample):
        f"{simulation_result}"
