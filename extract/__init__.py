import os
import tarfile


class ExtractException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __unicode__(self):
        return u"Extract Exception %d: %s" % (self.code, self.msg)

    def __str__(self):
        return unicode(self).encode('utf-8')


def extract(infile, outfile, verbose):
    infile = infile.strip()
    if not os.path.exists(infile):
        raise ExtractException(200, u"Input archive file does not exist: '%s'" % infile)
    if not tarfile.is_tarfile(infile):
        raise ExtractException(201, u"Input archive file does not appear to be a valid tar file: '%s'" % infile)
    if outfile is not None:
        outfile = outfile.strip()
        if os.path.isfile(outfile):
            raise ExtractException(202, u"The output must be a directory and cannot be a file: '%s'" % outfile)
        if not os.path.exists(outfile):
            raise ExtractException(203, u"The output directory does not exist: '%s'" % outfile)
    else:
        outfile = os.path.split(infile)[0]
    if verbose:
        print "Extracting '%s' to %s" % (infile, outfile)
    with tarfile.open(infile) as tar:
        tar.extractall(path=outfile)