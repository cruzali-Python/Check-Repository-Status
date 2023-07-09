from colorama import Fore, Style
from git import Repo
import os


def check_project_status(repo_dir):

    try:
        # Abre repo
        repo = Repo(repo_dir)

        # Get Estatus Repo
        repo_status = repo.git.status()

        # Verificar si hay cambios sin commit / push
        if 'Changes not staged for commit' in repo_status or 'Your branch is ahead of' in repo_status:
            print(
                f"{Fore.YELLOW}Proyecto '{repo_dir}': Pendiente de commit y/o push{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Proyecto '{repo_dir}': Actualizado{Style.RESET_ALL}")

    except Exception as e:
        print(
            f"{Fore.RED}Error al abrir el repositorio '{repo_dir}': {str(e)}{Style.RESET_ALL}")


def search_projects(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for directory in dirs:
            repo_dir = os.path.join(root, directory)
            check_project_status(repo_dir)


# Solicitar al usuario la ruta donde buscar
# r'C:\Users\user\Desktop\folder-proj'
carpeta_repositorios = input("Ingrese la ruta de repositorios:")

# validar si el path es valido
if not os.path.isdir(carpeta_repositorios):
    print(f"{Fore.LIGHTRED_EX}La ruta especificada no es una carpeta valida{Style.RESET_ALL}")
    exit()

# Ejecutar la busqueda de proyectos en carpeta principal y subcarpetas
search_projects(carpeta_repositorios)

# end
