
# AspectPy 0.1 — Aspect-Oriented Programming for Python

AspectPy brings AspectJ-style pointcuts to Python using a simple,
declarative and pythonic syntax.

## Example

```python
from aspectpy import pointcut, aspect

@pointcut("execution: example.services.* -> get_*")
def service_calls():
    pass

@aspect(service_calls)
def audit(jp):
    print("Calling:", jp.func_name)
    return jp.proceed()
