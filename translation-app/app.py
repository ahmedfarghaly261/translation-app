# Main script to run the app (entry point)
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.main_gui import launch_gui

if __name__ == "__main__":
    launch_gui()