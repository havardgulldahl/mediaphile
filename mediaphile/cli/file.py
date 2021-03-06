#!/usr/bin/env python
import logging

import sys
from optparse import OptionParser, OptionGroup
from mediaphile.cli import add_common_options, check_common_options
from mediaphile.lib.file_operations import find_duplicates


def main():
    """
    Command-line interface for using the file related features of photofile.
    """
    parser = OptionParser()

    common_group = OptionGroup(parser, "Common parameters")
    common_group.add_option("-s", "--source", dest="source", help="the source folder to process")
    common_group.add_option("-t", "--target", dest="target", help="the target folder for new files")
    common_group.add_option("--dry-run", dest="dry_run", action="store_true",
                            help="Just do a test-run. No actual changes will be made.")
    parser.add_option_group(common_group)

    duplicate_group = OptionGroup(parser, "Duplicate handling")
    duplicate_group.add_option("-d", "--find_duplicates", action="store_true",
                               help="locates duplicates in source folder compared to target folder",
                               dest="find_duplicates")
    duplicate_group.add_option("-x", "--delete_duplicates", action="store_true", dest="delete",
                               help="deletes any duplicate file from source folder found in both source and target folder")
    duplicate_group.add_option("-r", "--rename", action="store_true", dest="rename",
                               help="renames any duplicate file in the source folder found in both source and target folder")
    parser.add_option_group(duplicate_group)

    new_content_group = OptionGroup(parser, "Finding new files")
    new_content_group.add_option("-n", "--new_files",
                                 help="locates new files in source folder compared to target folder",
                                 dest="new_files")
    parser.add_option_group(new_content_group)

    add_common_options(parser)
    (options, args) = parser.parse_args()
    check_common_options(options, args)

    if options.delete and options.rename:
        print("Error: you cannot delete and rename in the same process. Chose one.")
        sys.exit(1)

    if not options.source and not options.target:
        print("ERROR: You must supply both source- and target-folders.\n")
        sys.exit(1)

    print(vars(options))

    if options.find_duplicates:
        list(find_duplicates(
            options.source,
            options.target,
            delete_duplicates=options.delete,
            rename_duplicates=options.rename,
            dry_run=options.dry_run,
            verbose=options.verbose
        ))


if __name__ == "__main__":
    main()