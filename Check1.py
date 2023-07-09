import os
from git import Repo
from colorama import Fore, Style

# Solicitar al usuario la ruta donde buscar
# r'C:\Users\user\Desktop\folder-proj'
carpeta_repositorios = input("Ingrese la ruta de repositorios:")

# validar si el path es valido
if not os.path.isdir(carpeta_repositorios):
    print(f"{Fore.LIGHTRED_EX}La ruta especificada no es una carpeta valida{Style.RESET_ALL}")
    exit()

# Iterar sobre los repositorios en la carpeta
for repo_path in os.listdir(carpeta_repositorios):
    repo_dir = os.path.join(carpeta_repositorios, repo_path)

    try:
        # Abrir el repositorio
        repo = Repo(repo_dir)

        # Obtener el estado del repositorio
        repo_status = repo.git.status()

        # Ramas
        branch_output = repo.git.branch('-a')

        # Verificar si hay cambios sin commitear o commits sin hacer push
        if 'Changes not staged for commit' in repo_status or 'Your branch is ahead of' in repo_status:
            print(
                f"{Fore.YELLOW}Proyecto '{repo_path}': Pendiente de commit y/o push{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Proyecto '{repo_path}': Actualizado{Style.RESET_ALL}")

        print(f"Ramas '{repo_path}':")
        print(branch_output)
        print()

    except Exception as e:
        print(
            f"{Fore.RED}Error al abrir el repositorio '{repo_path}': {str(e)}{Style.RESET_ALL}")
        print()
