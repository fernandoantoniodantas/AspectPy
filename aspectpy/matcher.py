# aspectpy/matcher.py
# Matches functions/modules against a PointcutSpec

import fnmatch
import inspect
from types import ModuleType
from aspectpy.parser import PointcutSpec


def matches_pointcut(spec: PointcutSpec, obj) -> bool:
    """
    Returns True if 'obj' (a function) matches the given PointcutSpec.
    """

    # If spec is missing or we are inspecting something that isn't a function: skip
    if spec is None:
        return False

    if not inspect.isfunction(obj):
        return False

    # ----------------------------------------------------
    # 1. Extract module path of the function
    # ----------------------------------------------------
    module = obj.__module__                # e.g. "examples.simple_service.service"
    module_parts = module.split(".")       # e.g. ["examples","simple_service","service"]

    # ----------------------------------------------------
    # 2. Compare module pattern segments
    # ----------------------------------------------------
    if len(module_parts) < len(spec.module_segments):
        return False

    for i, segment in enumerate(spec.module_segments):
        if segment == "*":
            continue
        if segment == "**":
            return True
        if module_parts[i] != segment:
            return False

    # ----------------------------------------------------
    # 3. Compare function name
    # ----------------------------------------------------
    func_name = obj.__name__               # e.g. "get_user"
    pattern = spec.function_pattern        # e.g. "get_*"

    if pattern is None:
        return True

    return fnmatch.fnmatch(func_name, pattern)
