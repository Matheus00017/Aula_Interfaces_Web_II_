s = input("Senha: ")

mai = min_ = num = False
for ch in s:
    if ch.isupper(): mai = True
    elif ch.islower(): min_ = True
    elif ch.isdigit(): num = True

ok = len(s) >= 8 and mai and min_ and num
print("Forte ✔" if ok else "Fraca ❌")
print("Regras:\n",
      "8+ caracteres" if ok else "precisa ter mais de 8 caracteres\n",
      "Mai" if mai else "precisa conter letras Maiúsculas\n",
      "Min" if min_ else "precisa conter Minúsculas\n",
      "Num" if num else "precisa conter Números")