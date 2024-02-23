#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
from glob import glob
from os.path import join, isfile, isdir, abspath


def get_bytes_from_file(file_path, num: int = 1) -> bytes:
	with open(file_path, "rb") as f:
		return f.read(num)


def main(args):
	try:
		if args.hex:
			header_bytes = bytes.fromhex(args.header)
		else:
			header_bytes = args.header.encode("ascii")
	except UnicodeEncodeError:
		print("Invalid header string", file=sys.stderr)
		sys.exit(1)
	except ValueError:
		print("Invalid hex header string", file=sys.stderr)
		sys.exit(1)

	byte_num = len(header_bytes)
	if args.recursive:
		print("Recursively l", end="", file=sys.stderr)
	else:
		print("L", end="", file=sys.stderr)

	print(f"ooking for {byte_num} bytes: {header_bytes}", file=sys.stderr)

	for fp in args.input:
		fp = abspath(fp)
		if isfile(fp):
			file_list = [fp]
		elif isdir(fp):
			file_list = glob(join(fp, "**", "*"), recursive=args.recursive, include_hidden=True)
			file_list = filter(lambda file: isfile(file), file_list)
		else:
			print(f"Cannot resolve {fp}", file=sys.stderr)
			continue

		for f in file_list:
			b = get_bytes_from_file(f, byte_num)
			# print(b, header_bytes)
			if b == header_bytes:
				print(f)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="find files based on their headers")
	parser.add_argument("header", type=str, help="the header to look for (must be ascii)")
	parser.add_argument("input", type=str, nargs="+", help="the files or folders to scan")

	parser.add_argument("-r", "--recursive", action="store_true", help="scan folders recursively")
	parser.add_argument("-x", "--hex", action="store_true", help="parse header as hex string (see https://docs.python.org/3/library/stdtypes.html#bytes.fromhex)")

	main(parser.parse_args())
