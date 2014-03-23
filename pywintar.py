import argparse
import sys
import archive
import extract


def parse_args():
    parser = argparse.ArgumentParser(description="Simple tar file utility for Windows")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    # if the action is to archive, we can give the user some options on the output compression
    parser.add_argument("-c", "--compression", choices=["gz", "bz2", "tar"], type=str, default="gz",
                        help="the output compression type if archiving files - defaults to 'gz'")
    parser.add_argument("-a", "--action", choices=["extract", "archive"], required=True, type=str,
                        help="the action to perform")
    parser.add_argument("-i", "--input", required=True, type=str,
                        help="the input archive if extracting, or the output archive if archiving")
    parser.add_argument("-o", "--output", type=str, default=None,
                        help="the output filename if archiving, or the output directory if extracting")
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        if args.action == "extract":
            if args.verbose:
                print "Extracting archive"
            extract.extract(infile=args.input, outfile=args.output, verbose=args.verbose)
        elif args.action == "archive":
            if args.verbose:
                print "Creating archive"
            archive.archive(infile=args.input, compression=args.compression, outfile=args.output, verbose=args.verbose)
    except (extract.ExtractException, archive.ArchiveException) as ex:
        print >> sys.stderr, ex.msg
        return ex.code
    return 0


if __name__ == "__main__":
    retval = main()
    sys.exit(retval)