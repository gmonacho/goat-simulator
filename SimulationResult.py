from SimulationException import BadSample
from SimulationModel import SuccessFailureDict, ESimulationType, ESIMULATION_TYPE_DESCRIPTION_MAPPING, \
    ESimulationObject, ESIMULATION_OBJECT_RESULT_KEYS_MAPPING


class SimulationResult:

    def __init__(self):
        self._results: dict[ESimulationType, SuccessFailureDict] = {
            data.value: SuccessFailureDict(success_count=0, failure_count=0)
            for data in ESimulationType
        }

    def __str__(self) -> str:
        msg: str = f"Simulation results:\n"
        for data in ESimulationType:
            try:
                success_count: int = self._results[data.value]['success_count']
                failure_count: int = self._results[data.value]['failure_count']
                total_count: int = success_count + failure_count
                msg += (f"\t{data.name} (`{ESIMULATION_TYPE_DESCRIPTION_MAPPING[data.value]}`):\n"
                        f"\t\tSuccess (Car): {success_count}\tRate: {success_count / total_count}\n"
                        f"\t\tFailure (Goat): {failure_count}\tRate: {failure_count / total_count}\n")
            except ZeroDivisionError as err:
                raise BadSample(f"Zero simulations performed yet (simulation {data.value}") from err
        return msg

    def add_one_point_to_simulation_type(self, simulation_type: ESimulationType, simulation_object: ESimulationObject):
        self._results[simulation_type][ESIMULATION_OBJECT_RESULT_KEYS_MAPPING[simulation_object]] += 1
