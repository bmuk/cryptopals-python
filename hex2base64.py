#!/usr/bin/env python3

import sys
import argparse

def getArgs():
    """This handles getting input from arguments - stdin is handled by main."""
    parser = argparse.ArgumentParser(description="Convert hexadecimal to base64.")
    parser.add_argument("hex", type=str, nargs="*", help="Hexadecimal input to be processed")
    args = parser.parse_args()
    return args.hex

def main():
    args = getArgs()
    if args == []:
        for line in iter(sys.stdin.readline, ''):
            print(line)
    else:
        for arg in args:
            print(arg)

main()
