import subprocess


def verificar_e_instalar(biblioteca):
    # Verifica se a biblioteca está instalada
    resultado = subprocess.run(['pip', 'show', biblioteca], capture_output=True)
    # Se o código de retorno for diferente de zero, significa que a biblioteca não foi encontrada
    if resultado.returncode != 0:
        # Tenta instalar a biblioteca com o argumento --user
        resultado = subprocess.run(['pip', 'install', '--user', biblioteca], capture_output=True)
        # Se o código de retorno for diferente de zero, significa que ocorreu um erro na instalação
        if resultado.returncode != 0:
            # Imprime a mensagem de erro
            print(resultado.stderr.decode())
            return False
        else:
            # Imprime a mensagem de sucesso
            print(resultado.stdout.decode())
            return True
    else:
        # Imprime a mensagem de que a biblioteca já está instalada
        print(f'{biblioteca} já está instalada.')
        return True


verificar_e_instalar('pwinput')
