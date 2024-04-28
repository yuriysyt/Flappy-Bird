"""
This class provides functionality for sorting levels 
based on their completion status.

sorting_cfg: Reads a configuration file containing level completion statuses, 
sorts the levels based on their completion status, 
and returns a list of sorted levels.


"""
import re
class LevelSorter:
    @staticmethod
    def sorting_cfg(filename):
        """
        Reads a configuration file containing level completion statuses, 
        sorts the levels based on their completion status,
        and returns a list of sorted levels.
        
        Args: filename (str): The path to the configuration file.
        
        Returns: list: A list of strings representing the sorted levels 
                       along with their completion statuses.
        
        """
        levels = {}
        sorted_levels = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line and '=' in line:
                    key, value = line.split('=')
                    passed = value.strip() == "True"
                    level_number = re.search(r'\d+', key).group()
                    if passed:
                        sorted_levels.append(f"Level {level_number}: Passed")
                    else:
                        sorted_levels.insert(0, f"Level {level_number}: Not Passed")
                    levels[key] = passed
        return sorted_levels

