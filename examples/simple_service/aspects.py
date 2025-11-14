from aspectpy import pointcut, aspect

@pointcut("execution: examples.simple_service.service -> get_*")
def service_calls():
    pass

@aspect(service_calls)
def audit(jp):
    print(f"[AUDIT] Chamando {jp.func_name} com args={jp.args}")
    result = jp.proceed()
    print(f"[AUDIT] Retornou {result}")
    return result
