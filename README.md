pywintar
========

A simple application to provide some Windows context menu support for tarballs and gzip/bzip2 tarballs in much the
same way it is supported for compressed folders. See screenshots:

![alt text](https://github.com/tristeng/pywintar/raw/master/res/right-click-folder.png "Compresion Context Menu")

![alt text](https://github.com/tristeng/pywintar/raw/master/res/right-click-tar.png "Extraction Context Menu")

Double clicking a .tar, .tar.gz or .tar.bz2 file will automatically expand the archive.

Why?
----

Whenever I'm on a Windows box and want to handle tarballs I usually install 7-Zip, but this is usually overkill for
my needs. I wanted a simple and fast way to expand my tarballs. As well, I also wanted the ability to create the
tarballs in the same way I could create zip files on Windows; by right-clicking the file or folder and sending it to a
compressed folder.

The Solution
------------

Python has an excellent tarfile package that allowed me to write a simple console application (less than 200 lines of
code) that can expand/compress files or folders into uncompressed tarballs, gzip tarballs or bzip2 tarballs.

In order to make it portable (no Python install needed), I then used [cx_Freeze](http://cx-freeze.sourceforge.net/) to
compile the python code into an executable.

Finally, I used [Inno Setup](http://www.jrsoftware.org/isinfo.php) to bundle the compiled code into an installer that
modifies the registry to add in the context menus.

Installation
------------

### Pre-requisites

* [Microsoft Visual C++ Redistributable Package](http://www.microsoft.com/download/en/details.aspx?id=29) if you have
MS Visual Studio installed, you likely already have this

Download an installer from the releases page and run it or you can build a installer your self:

1. clone the repository
2. build the application with [cx_Freeze](http://cx-freeze.sourceforge.net/)
3. generate an installer using [Inno Setup](http://www.jrsoftware.org/isinfo.php) and the innosetup/setup.iss file

**WARNING:** The installer will modify your registry in order to add the context menus. If you already have another
application that uses context menus for .tar, .gz or .bz2 files then those menus may no longer appear. If you wish to
restore the other applications menus, you may have to re-install the application. See the innosetup/setup.iss file for
the registry changes.

TODO
----

* Add in support for the installer to automatically install the Microsoft Visual C++ Redistributable Package if it
hasn't already been installed
* Make a 64 bit version - not sure if the 32-bit application can handle large tarballs
* Figure out how to get the "Send to" commands under the "Send to" menu already available throught stock Windows
* Right now it will fail silently - should probably have an alert popup upon error