# the .home syntax directs the program to find the module named 'home' in the current directory
# then we import the bp object but rename it home for this file
from .home import bp as home

from .dashboard import bp as dashboard