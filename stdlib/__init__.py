def _stdlib():
    import imp, distutils.sysconfig

    LIBDEST = distutils.sysconfig.get_config_var("LIBDEST")
    LIB = distutils.sysconfig.get_python_lib()

    class _Stdlib(object):

        def __getattr__(self, name):
            (fObj, filename, (suffix, mode, type)) = imp.find_module(name)
            print 'name:', fObj, filename, suffix, mode, type
            if fObj is None and not filename.startswith("/"):
                # It is a builtin module.  Great.
                stdlib = True
            elif filename.startswith(LIB + "/"):
                # It is a module in site-packages.  You cannot get it from here.
                # This check comes first in case LIB is a child of LIBDEST (which
                # it typically is).
                stdlib = False
            elif filename.startswith(LIBDEST + "/"):
                # It is a stdlib module probably!
                stdlib = True
            else:
                # It is from some other random place on the path.
                stdlib = False

            if fObj is not None:
                fObj.close()

            if stdlib:
                return __import__(name)
            raise ImportError("No module named %s" % (name,))

    return _Stdlib()

import sys
sys.modules["stdlib"] = _stdlib()
