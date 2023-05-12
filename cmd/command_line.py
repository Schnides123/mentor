import argparse

from lib.loaders import repo_loader, file_loader
from lib.prompter import enriched_prompt


def command_line():
    parser = argparse.ArgumentParser(prog='mentor', description="An AI assisted mentor!")
    subp = parser.add_subparsers(dest='subparser_name')

    # create sub-parser for load_command
    load_parser = subp.add_parser("load", help="Loads a file")

    # create -s flag for source, can either be a path or repository
    load_parser.add_argument("-s", "--source", type=str,
                             metavar="source", help="Specifies the source of the file to be loaded.")

    load_parser.add_argument("-t", "--type", type=str,
                             metavar="type", default="repo", help="Specifies the resource type being loaded.")

    load_parser.add_argument("-b", "--branch", type=str,
                             metavar="branch", default="master",
                             help="Specifies the branch to load for a repo")

    # create a sub-parser for sending prompts
    prompt_parser = subp.add_parser("prompt", help="Send a prompt and print the response")

    prompt_parser.add_argument("prompt")
    prompt_parser.add_argument("-f", "--format", type=str,
                               metavar="format",
                               help="Specifies the format to return the answer as (json, markdown, etc.)")

    # parse the arguments from standard input
    args = parser.parse_args()
    # calling functions depending on type of argument
    if args.subparser_name is not None:
        if args.subparser_name == "load":
            load(args)
        if args.subparser_name == "prompt":
            print(f"  >> {args.prompt}")
            print(enriched_prompt(args.prompt, args.format or "markdown")["answer"])
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
