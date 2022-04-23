primeiroNome = input("digite o seu primeiro nome: ")
("Digite seu salário print do mês de abril: ")
salárioreais = input("Reais: ")
saláriocentavos = input("centavo: ")
salárioformatado = salárioreais + "," + saláriocentavos
primeiraletra = primeiroNome [ 0:1].upper()
restantenome = primeiroNome [1:].lower()
primeiroNomeformatado = primeiraletra + restantenome
mensagem = "o salário de " + primeiroNomeformatado + "no mês de abril foi de R$" + salárioformatado + "."
print ( mensagem)
