from modules.logger.log import Logger
from x64.network.alive import Connection
from data.banner.banner import DisplayBanner
from core.console_scripts.exit import ExitConsole
from core.console_scripts.clear import ClearScreen

class Worker:
    """
    A class representing a worker.

    Methods:
        __init__: Initializes the Worker class.
        main: The main method for the worker's functionality.
    """

    def __init__(self) -> None:
        """
        Initializes the Worker class.
        """
        pass

    @staticmethod
    def main() -> None:
        """
        The main method for the worker's functionality.

        This method should contain the main functionality of the Worker class.
        """
        Logger.__client_logger__("Testing")


if __name__ == '__main__':
    try:
        ClearScreen.clear()
        DisplayBanner.show()
        Connection.check_wifi()
        Worker.main()
    except KeyboardInterrupt:
        """
        Handle keyboard interrupt gracefully.

        If a KeyboardInterrupt occurs, log the event and exit the program.
        """
        ExitConsole.exit()