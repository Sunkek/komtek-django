"""Some logic functions from views.py"""

def format_version(string):
    """Format version input from 1.1 to 01.01.00"""
    version = [i.zfill(2) for i in string.split(".")] + ["00", "00"]
    return ".".join(version[:3])
