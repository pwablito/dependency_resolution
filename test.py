#!/usr/bin/env python3

import src.input as input_util


def main():
    input_util.InputFile("test/progs.json").to_graph().resolve("prog1")


if __name__ == "__main__":
    main()
