from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        pass

    @abstractmethod
    def get_destination(self) -> str:
        pass


class ConsoleLogger(Logger):
    def log(self, level: str, message: str) -> None:
        # TODO: print "[level] message" to console
        print(f'[{level}] {message}')
        

    def get_destination(self) -> str:
        # TODO: return "Console"
        return "Console"


class FileLogger(Logger):
    def __init__(self, file_path: str):
        # TODO: initialize self._file_path
        self._file_path = file_path
        pass

    def log(self, level: str, message: str) -> None:
        # TODO: print "Writing to file_path: [level] message"
        print(f'Writing to {self._file_path}: [{level}] {message}')
        pass

    def get_destination(self) -> str:
        # TODO: return "File: file_path"
        return f"File: {self._file_path}"


class DatabaseLogger(Logger):
    def __init__(self, table_name: str):
        # TODO: initialize self._table_name
        self._table_name=table_name
       

    def log(self, level: str, message: str) -> None:
        # TODO: print "INSERT INTO table_name: [level] message"
        print(f'INSERT INTO {self._table_name}: [{level}] {message}')

    def get_destination(self) -> str:
        # TODO: return "Database: table_name"
        return f"Database: {self._table_name}"


class Application:
    def __init__(self, logger: Logger):
        # TODO: initialize self._logger
        self._logger = logger
        pass

    def run(self):
        # TODO: log three messages with level "INFO":
        #   "Application starting..."
        #   "Processing data..."
        #   "Application shutting down."
        self._logger.log("INFO", "Application starting...")
        self._logger.log("INFO", "Processing data...")
        self._logger.log("INFO", "Application shutting down.")



if __name__ == "__main__":
    loggers = [
        ConsoleLogger(),
        FileLogger("/var/log/app.log"),
        DatabaseLogger("app_logs"),
    ]

    for logger in loggers:
        print(f"--- Using {logger.get_destination()} ---")
        app = Application(logger)
        app.run()
        print()