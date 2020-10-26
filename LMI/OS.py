from . import LMI
import platform


def getLMAddress():
    return hex(id(LMI.luciferManager))


def getOS(query=None):
    if "OSInfo" not in LMI.cache:
        OSInfo = {
            "machine": platform.machine(),
            "node": platform.node(),
            "processor": platform.processor(),
            "python_build": platform.python_build(),
            "python_compiler": platform.python_compiler(),
            "python_branch": platform.python_branch(),
            "python_implementation": platform.python_implementation(),
            "python_revision": platform.python_revision(),
            "python_version": platform.python_version(),
            "python_version_tuple": platform.python_version_tuple(),
            "release": platform.release(),
            "system": platform.system(),
            "version": platform.version(),
            "uname": platform.uname()
        }
        LMI.cache["OSInfo"] = OSInfo
    else:
        OSInfo = LMI.cache["OSInfo"]
    if "java" in OSInfo["system"].lower():
        OSInfo["java_version"] = platform.java_ver()
    elif "windows" in OSInfo["system"].lower():
        OSInfo["win32_version"] = platform.win32_ver()
    elif "mac" in OSInfo["system"].lower():
        OSInfo["mac_version"] = platform.mac_ver()
    elif ("unix" in OSInfo["system"].lower()) or ("linux" in OSInfo["system"].lower()):
        OSInfo["libc_version"] = platform.libc_ver()
    if query is not None:
        if query in OSInfo.keys():
            return 1, OSInfo[query]
        return 0, "Query Not Found"
    return 1, OSInfo
