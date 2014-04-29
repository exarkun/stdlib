import os.path

from setuptools import setup

path = os.path.join(os.path.dirname(__file__), b"stdlib/version")
with open(path) as fObj:
    version = fObj.read().strip()
del path

setup(
    # This is the human-targetted name of the software being packaged.
    name="stdlib",
    # This is a string giving the version of the software being packaged.  For
    # simplicity it should be something boring like X.Y.Z.
    version=version,
    # This identifies the creators of this software.  This is left symbolic for
    # ease of maintenance.
    author="Jean-Paul Calderone",
    # This is contact information for the authors.
    author_email="exarkun@twistedmatrix.com",
    # Here is a website where more information about the software is available.
    url="http://github.com/exarkun/stdlib",

    # This defines *Python* packages (in other words, things that can be
    # imported) which are part of the package.  Most of what they contain will
    # be included in the package automatically by virtue of the packages being
    # mentioned here.  These aren't recursive so each sub-package must also be
    # explicitly included.
    packages=[
        "stdlib",
        ],

    # This defines extra non-source files that live in the source tree that
    # need to be included as part of the package.
    package_data={
        # This is the canonical definition of the source form of the cluster
        # version
        "stdlib": ["version"],
        },
    )
