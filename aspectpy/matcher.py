# aspectpy/matcher.py
def matches_pointcut(pointcut, func):

    expr = pointcut.expression
    # In the moment, only a very simple matching is implemented => execution: module.* -> *
    # after that we integrate ANTLR parser.
    if not expr.startswith("execution:"):
        return False

    return True  # placeholder
