import argparse

from lib.loaders import repo_loader, file_loader


def command_line():
    parser = argparse.ArgumentParser(prog='mentor', description="An AI assisted mentor!")
    subp = parser.add_subparsers(dest='subparser_name')

    # create sub-parser for load_command
    load_parser = subp.add_parser('load', help="Loads a file")

    # create -s flag for source, can either be a path or repository
    load_parser.add_argument("-s", "--source", type=str,
                             metavar="source", help="Specifies the source of the file to be loaded.")

    load_parser.add_argument("-t", "--type", type=str,
                             metavar="type", default="repo",
                             help="Specifies the resource type being loaded.")

    load_parser.add_argument("-b", "--branch", type=str,
                             metavar="branch", default="master",
                             help="Specifies the branch to load for a repo")

    # parse the arguments from standard input
    args = parser.parse_args()
    # calling functions depending on type of argument
    if args.subparser_name is not None:
        if args.subparser_name == "load":
            load(args)
    else:
        # display help message when no arguments are specified
        parser.print_help()


def load(args):
    if args.type is None:
        print("specify a type of resource to load")
        return
    if args.source is None:
        print("specify a path or URL to load")
        return
    if args.type == "repo":
        repo_loader.load(args.source, args.branch)
    if args.type == "file":
        file_loader.load(args.source)
