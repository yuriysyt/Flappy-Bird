"""
The LevelSorter class is responsible for sorting levels 
based on their completion status.

sorting_cfg: Reads a configuration file 
and sorts the levels into two categories: passed and not passed.
    - filename: The name of the configuration file to read.
    - Returns a list of sorted levels, with not passed levels listed first, 
      followed by passed levels.

"""

import os
import re

class LevelSorter:
    @staticmethod
    def sorting_cfg():
        current_dir = os.getcwd()
        config_file_path = os.path.join(current_dir, "config.cfg")
        levels = {}
        not_passed_levels = []
        passed_levels = []
        sorted_levels = []

        if os.path.exists(config_file_path):
            with open(config_file_path, 'r') as file:
                for line in file:
                    line = line.rstrip()
                    if line and '=' in line:
                        key, value = line.split('=')
                        passed = value.strip() == "True"
                        level_number = re.search(r'\d+', key).group()

                        if passed:
                            passed_levels.append(level_number)
                        else:
                            not_passed_levels.append(level_number)

                        levels[key] = passed

                for level_number in not_passed_levels:
                    sorted_levels.append(f"Level {level_number}: Not Passed")

                for level_number in passed_levels:
                    sorted_levels.append(f"Level {level_number}: Passed")

        return sorted_levels