from cmd.command_line import command_line
from src import load_environment_variables

if __name__ == "__main__":
    load_environment_variables()
    command_line()
