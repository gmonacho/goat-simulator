import json
import logging
import sys
from collections.abc import Sequence
from random import randint

from SimulationException import BadSample
from SimulationModel import ESimulationObject, ESimulationType
from SimulationResult import SimulationResult

logger = logging.getLogger()
logging.basicConfig(stream=sys.stdout)
for h in logger.handlers:
    h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
logger.setLevel('DEBUG')


class SimulationBase:

    def __init__(self, door_count: int):
        self._doors: list[ESimulationObject] = [ESimulationObject.GOAT for _ in range(door_count)]
        self._doors[randint(0, len(self._doors) - 1)] = ESimulationObject.CAR
        logger.debug(f"Doors : {json.dumps(self._doors)}")
        self._result = SimulationResult()

    @property
    def results(self) -> SimulationResult:
        return self._result

    def _get_a_random_door(self) -> tuple[int, ESimulationObject]:
        """
        get a random door
        :return: tuple containing door index and ESimulationObject
        """
        index = randint(0, len(self._doors) - 1)
        return index, self._doors[index]

    def _get_doors_except_indexes(self, indexes: Sequence[int]) -> list[ESimulationObject]:
        """
        get every door values except specified doors
        :param indexes: indexes of door to except
        :return: every door values except specified doors
        """
        return [obj for i, obj in enumerate(self._doors) if i not in indexes]

    def _get_a_random_door_except_indexes(self, indexes: Sequence[int]):
        """
        get a random door between doors except specified doors
        :param indexes: index of doors to except
        :return: a random door between doors except specified doors
        """
        other_doors: list[ESimulationObject] = self._get_doors_except_indexes(indexes=indexes)
        index = randint(0, len(other_doors) - 1)
        return index, other_doors[index]

    def _get_a_goat_index_except_indexes(self, indexes: Sequence[int]):
        """
        get a random goat index except specified doors
        :param indexes: index of doors to except
        :return: a random goat index except specified doors
        """
        goat_doors_indexes = [
            i for i, obj in enumerate(self._doors) if obj == ESimulationObject.GOAT and i not in indexes
        ]
        if not goat_doors_indexes:
            raise BadSample("There is only cars behind the doors")
        return goat_doors_indexes[randint(0, len(goat_doors_indexes) - 1)]

    def simulate_a_door_opening(self):
        """
        simply simulate a door opening and add save simulation result to results property
        """
        self._result.add_one_point_to_simulation_combination(ESimulationType.OPEN_DIRECTLY,
                                                             self._get_a_random_door()[1])

    def simulate_a_door_opening_after_showing_a_goat(self):
        """
        simulate a door opening following that rules :
        "Chose a door -> show a goat (another door than chosen one) -> Chose a random door between doors except showed door",
        and save result to results property
        """
        selected_index: int = self._get_a_random_door()[0]
        showed_goat_index: int = self._get_a_goat_index_except_indexes(indexes=[selected_index])

        selected_door = self._get_a_random_door_except_indexes(indexes=[showed_goat_index])

        self._result.add_one_point_to_simulation_combination(ESimulationType.OPEN_AFTER_SHOWING_A_GOAT,
                                                             selected_door[1])

    def simulate_another_door_opening_after_selected_one_another(self):
        """
        simulate a door opening following that rules :
        Chose a door -> show a goat (another door than chosen one) -> Chose the third door
        and save result to results property
        """
        selected_door_index: int = self._get_a_random_door()[0]

        showed_goat_index: int = self._get_a_goat_index_except_indexes(indexes=[selected_door_index])

        selected_door = self._get_a_random_door_except_indexes(indexes=[showed_goat_index, selected_door_index])

        self._result.add_one_point_to_simulation_combination(ESimulationType.OPEN_THE_OTHER_DOOR_AFTER_SHOWING_A_GOAT,
                                                             selected_door[1])
