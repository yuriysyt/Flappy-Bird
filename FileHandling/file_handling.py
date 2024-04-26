import configparser

class FileHandler:
    def __init__(self, filename="config.cfg"):
        self.filename = filename
        self.config = configparser.ConfigParser()
        if not self.config.read(self.filename):
            self.initialize_config()

    def initialize_config(self):
        self.config["Levels"] = {"level_{}".format(i): "False" for i in range(1, 6)}
        with open(self.filename, "w") as config_file:
            self.config.write(config_file)

    def is_level_completed(self, level_name):
        return self.config.getboolean("Levels", level_name)

    def set_level_completed(self, level_name, completed=True):
        self.config.set("Levels", level_name, str(completed))
        with open(self.filename, "w") as config_file:
            self.config.write(config_file)
