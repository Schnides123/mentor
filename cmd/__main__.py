from cmd.command_line import command_line
from lib.environment_variables import load_environment_variables


def run():
    load_environment_variables()
    command_line()


if __name__ == "__main__":
    run()
