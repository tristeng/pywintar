import os
import tarfile
import re

_comp = dict(gz=dict(ext=".tar.gz", mode="w:gz"),
             bz2=dict(ext=".tar.bz2", mode="w:bz2"),
             tar=dict(ext=".tar", mode="w"))
_ext_re = re.compile(r"(?:_\d{3})?\.tar(?:\.(gz|bz2))?$", re.I)


class ArchiveException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __unicode__(self):
        return u"Archive Exception %d: %s" % (self.code, self.msg)

    def __str__(self):
        return unicode(self).encode('utf-8')


def _strip_ext(filename):
    """
    Strips off .tar, .tar.gz or .tar.bz2 extensions and then any futher extension
    """
    filename = _ext_re.sub("", filename)
    return os.path.splitext(filename)[0]


def _gen_outfilename(infile, ext, outfile, verbose=False):
    # if no outfile was specified - generate one based on the infile
    if outfile is None:
        if os.path.isdir(infile):
            base = infile.rstrip("\\/") + ext
        elif os.path.isfile(infile):
            base = _strip_ext(infile) + ext
        else:
            # not sure if this is possible on Windows...maybe if it's a symbolic link?
            raise ArchiveException(102, u"Input file is neither a directory or file: '%s'" % infile)
    else:  # replace any extension the user supplied with one matching the compression
        base = _strip_ext(outfile.rstrip("\\/")) + ext
    counter = 0
    while os.path.exists(base):
        if verbose:
            print "Existing path '%s' exists" % base
        counter += 1
        if counter >= 1000:
            raise ArchiveException(103, u"Attempted to create a unique output filename based on input filename 1000 "
                                        u"times but failed: '%s'" % infile)
        base = _strip_ext(base) + "_%03d" % counter + ext
        if verbose:
            print "Attempting to use '%s' instead" % base
    return base


def archive(infile, compression, outfile, verbose=False):
    # error checking
    # make sure the input file/dir actually exists
    infile = infile.strip()
    if outfile is not None:
        outfile = outfile.strip()
    if not os.path.exists(infile):
        raise ArchiveException(100, u"The input file/directory does not exist: '%s'" % infile)
    # make sure compression is valid
    if compression not in _comp:
        raise ArchiveException(101, u"Unrecognized compression type: '%s'" % compression)
    comp = _comp[compression]
    # generate a valid output file name
    outfile = _gen_outfilename(infile, comp["ext"], outfile, verbose)
    if verbose:
        print "Adding '%s' to archive '%s'" % (infile, outfile)
    with tarfile.open(name=outfile, mode=comp["mode"]) as tar:
        tar.add(infile, arcname=os.path.basename(infile))