from enum import IntEnum
from typing import TypedDict, Literal
from collections.abc import Mapping

SuccessFailureDict = TypedDict("SuccessFailureDict", {
    "success_count": int,
    "failure_count": int,
})


class ESimulationType(IntEnum):
    OPEN_DIRECTLY = 1
    OPEN_AFTER_SHOWING_A_GOAT = 2
    OPEN_THE_OTHER_DOOR_AFTER_SHOWING_A_GOAT = 3


ESIMULATION_TYPE_DESCRIPTION_MAPPING: Mapping[ESimulationType, str] = {
    ESimulationType.OPEN_DIRECTLY:
    "Open a random door directly",
    ESimulationType.OPEN_AFTER_SHOWING_A_GOAT:
    "Chose a door -> show a goat (another door than chosen one) -> Chose a random door between doors except showed door",
    ESimulationType.OPEN_THE_OTHER_DOOR_AFTER_SHOWING_A_GOAT:
    "Chose a door -> show a goat (another door than chosen one) -> Chose the third door"
}


class ESimulationObject(IntEnum):
    GOAT = 1
    CAR = 2


ESIMULATION_OBJECT_RESULT_KEYS_MAPPING: Mapping[ESimulationObject, Literal['failure_count', 'success_count']] = {
    ESimulationObject.GOAT: 'failure_count',
    ESimulationObject.CAR: 'success_count'
}
