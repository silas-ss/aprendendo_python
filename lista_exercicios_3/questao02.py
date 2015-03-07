#!/usr/bin/python
# coding: latin-1

usuario = ""
senha = ""
while usuario.lower() == senha.lower():
   usuario, senha = raw_input("Usuário: "), raw_input("Senha: ")
   if usuario.lower() == senha.lower():
      print("A senha não pode ser igual ao nome de usuário!")
