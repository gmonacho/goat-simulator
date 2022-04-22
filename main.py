import logging
import sys

from SimulationBase import SimulationBase

logger = logging.getLogger()
logging.basicConfig(stream=sys.stdout)
for h in logger.handlers:
    h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
logger.setLevel('DEBUG')


class PayloadException(Exception):
    pass


def perform_goat_simulation(door_count: int, simulation_count: int):
    """
    populate a simulation with specified door_count and perform specified count goat simulations
    :param door_count: number of door to add to simulation
    :param simulation_count: number of simulation to perform
    then print the result on STDOUT
    """
    simulation_base = SimulationBase(door_count=door_count)

    logger.info("Performing simulations...")
    for i in range(simulation_count):
        simulation_base.simulate_a_door_opening()
        simulation_base.simulate_a_door_opening_after_showing_a_goat()
        simulation_base.simulate_another_door_opening_after_selected_one_another()

    logger.info(simulation_base)


if __name__ == "__main__":

    try:
        try:
            simulation_count = int(sys.argv[1])
        except IndexError as err:
            raise PayloadException("Missing simulation count argument") from err
        except Exception as err:
            raise PayloadException(f"Simulation count argument `{sys.argv[1]}` is invalid")

        perform_goat_simulation(door_count=3, simulation_count=simulation_count)

    except PayloadException as err:
        logger.info(f"Invalid Arguments `{err}`.\nUsage: program <simulation count: integer>")
    except Exception as err:
        logger.exception(f"An error occurred during execution : {err}")
