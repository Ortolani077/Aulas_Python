ano=int(input('Qual ano de nascimento do atleta? '))
div=2022-ano
if div<=9:

    print('O aluno tem {} anos, sua categoria é \033[34mMIRIM'.format(div))
elif div>9 and div<15:
    print('O aluno tem {} anos, sua categoria é \033[32mINFANTIL'.format(div) )
elif div>15 and div<20:
    print('O aluno te {} anos, sua categoria é \033[31mJUNIOR'.format(div))
elif div==20:
    print('O aluno tem {} anos, sua categoria é \033[33mSênior'.format(div))
else:
    print('O aluno tem {} anos, sua categoria é \033[35mMaster'.format(div))