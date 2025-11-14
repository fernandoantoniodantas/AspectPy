import examples.simple_service.aspects  # registra pointcut + aspect
from aspectpy.weaver import weave_all

from examples.simple_service.service import get_user

# aplica aspects nos módulos carregados
weave_all()

# agora a função já está interceptada
user = get_user(42)
print("Resultado final:", user)
