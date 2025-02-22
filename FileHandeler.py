import json
import os
from typing import List, Dict, Any


class FileHandler:
    """Handles reading and writing records to/from JSON files."""

    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    def read_records_file(self) -> List[Dict[str, Any]]:
        """Read records from the JSON file."""
        if not os.path.isfile(self.__file_name):
            return []
        try:
            with open(self.__file_name, "r", encoding="UTF-8") as file:
                return [json.loads(line) for line in file]
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error reading file: {e}")
            return []

    def write_record(self, records: List[Dict[str, Any]]) -> None:
        """Write records to the JSON file."""
        try:
            with open(self.__file_name, "w", encoding="UTF-8") as file:
                for record in records:
                    file.write(json.dumps(record) + "\n")
        except IOError as e:
            print(f"Error writing to file: {e}")

