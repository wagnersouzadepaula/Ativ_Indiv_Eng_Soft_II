# O python tem uma biblioteca padrão poderosa que fornece acesso a muitos módulos reutilizáveis.

import os
import sys
import datetime
import time
import html
print("\033[1;31m print(sys.platform): \033[0;0m")
print(sys.platform)
print("\033[1;31m print(sys.version): \033[0;0m")
print(sys.version)
print("\033[1;31m print(os.getcwd()): \033[0;0m")
print(os.getcwd())
print("\033[1;31m print(os.environ): \033[0;0m")
print(os.environ)
print("\033[1;31m print(os.getenv('HOME')): \033[0;0m")
print(os.getenv('HOME'))
print("\033[1;31m print(datetime.date.today()): \033[0;0m")
print(datetime.date.today())
print("\033[1;31m print(datetime.date.today().day): \033[0;0m")
print(datetime.date.today().day)
print("\033[1;31m print(datetime.date.today().month): \033[0;0m")
print(datetime.date.today().month)
print("\033[1;31m print(datetime.date.today().year): \033[0;0m")
print(datetime.date.today().year)
print("\033[1;31m print(time.strftime('%H:%M')): \033[0;0m")
print(time.strftime("%H:%M"))
print("\033[1;31m print(time.strftime('%A %p')): \033[0;0m")
print(time.strftime("%A %p"))
print("\033[1;31m print(html.escape('Este fragmento de HTML contem uma tag <script>script</script>.')): \033[0;0m")
print(html.escape("Este fragmento de HTML contem uma tag <script>script</script>."))
print("\033[1;31m print(html.unescape('Eu &hearts; as bibliotecas padrões do Python')): \033[0;0m")
print(html.unescape("Eu &hearts; as bibliotecas padrões do Python"))
