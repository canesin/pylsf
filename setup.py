"""

PyLSF: Python/Pyrex interface module to LSF Batch Scheduler

"""

from distutils.core import setup
from distutils.extension import Extension
from distutils.command import clean
from distutils.sysconfig import get_python_lib
from Pyrex.Distutils import build_ext

import os, re
import sys, platform
from string import *
from stat import *

# Mininmum of Python 2.3 required because that's what Pyrex-0.9.5 requires

if not hasattr(sys, 'version_info') or sys.version_info < (2,3,0,'final'):
   raise SystemExit, "Python 2.3+ or later required to build PyLSF."

# Retrieve the LSF environment variables and work out include dir

lsf_major = 2.1
lsf_incdir = "/opt/openlava-2.1/include"
lsf_libdir = os.getenv("LSF_LIBDIR")
include_dirs = [lsf_incdir, '/usr/include']
library_dirs = [lsf_libdir, '/usr/lib64', '/usr/lib']
extra_link_args = [ '']
extra_objects = [ '']

libraries = ['bat','lsf','nsl']

print "PyLSF: detected LSF version %d" % lsf_major
compiler_dir = os.path.join(get_python_lib(prefix=''), 'pylsf/')

# Trove classifiers

classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Natural Language :: English
Operating System :: POSIX :: Linux
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
"""

doclines = __doc__.split("\n")

setup(
    name = "PyLSF",
    version = "0.0.1",
    description = doclines[0],
    long_description = "\n".join(doclines[2:]),
    author = "Mark Roberts",
    author_email = "mark at gingergeeks co uk",
    url = "http://www.gingergeeks.co.uk/pylsf/",
    classifiers = filter(None, classifiers.split("\n")),
    platforms = ["Linux"],
    keywords = ["Batch Scheduler", "LSF"],
    packages = ["pylsf"],
    ext_modules = [
        Extension( "pylsf/pylsf",["pylsf/pylsf.pyx"],
                   libraries = libraries,
                   library_dirs = library_dirs,
                   include_dirs = include_dirs,
                   extra_compile_args = [],
                   extra_link_args = [] )
    ],
    cmdclass = {"build_ext": build_ext}
)

