"""
The FileHandler class is responsible for managing configuration files 
and level completion status.

__init__: Initializes the FileHandler with a default filename ('config.cfg') 
and checks if the configuration file exists. If not, it initializes the configuration.

initialize_config: Creates a new configuration file with default settings 
if one does not already exist.

is_level_completed: Checks if a specific level is marked 
as completed in the configuration file.

set_level_completed: Marks a level as completed in the configuration file, 
with an option to specify completion status.

"""

import configparser

class FileHandler:
    def __init__(self, filename="config.cfg"):
        self.filename = filename
        self.config = configparser.ConfigParser()
        if not self.config.read(self.filename):
            self.initialize_config()

    def initialize_config(self):
        self.config["Levels"] = {}
        for i in range(1, 6):
            self.config["Levels"][f"level_{i}"] = "False"
        with open(self.filename, "w") as config_file:
            self.config.write(config_file)

    def is_level_completed(self, level_name):
        return self.config.getboolean("Levels", level_name)

    def set_level_completed(self, level_name, completed=True):
        current_status = self.config.get("Levels", level_name)
        if not current_status == "True" and completed:
            self.config.set("Levels", level_name, str(completed))
            with open(self.filename, "w") as config_file:
                self.config.write(config_file)
