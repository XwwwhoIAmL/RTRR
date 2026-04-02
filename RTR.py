import time
import os
import ctypes
import webbrowser
import sys

# --- CONFIGURACIÓN DE COLORES PARA LA CONSOLA ---
BLUE = "\033[34m"
CYAN = "\033[36m"
WHITE = "\033[97m"
RED = "\033[91m"
MAGENTA = "\033[35m"
RESET = "\033[0m"

def is_admin():
    """Verifica si el programa tiene permisos de administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def rtr_banner():
    """Muestra el logo principal de RTR."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{BLUE}")
    print(r"""
    ██████╗ ████████╗██████╗ 
    ██╔══██╗╚══██╔══╝██╔══██╗
    ██████╔╝   ██║   ██████╔╝
    ██╔══██╗   ██║   ██╔══██╗
    ██║  ██║   ██║   ██║  ██║
    ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
    """)
    print(f"{CYAN}      [ SISTEMA UNIFICADO V3.0 ]")
    print(f"{WHITE}      BY: {MAGENTA}F H R E S S S C H O{RESET}")
    print(f"{BLUE}  _________________________________{RESET}\n")

def banner_field_cloud():
    """Banner grande para Field Cloud."""
    print(f"{CYAN}")
    print(r"""
    ███████╗██╗███████╗██╗     ██████╗ 
    ██╔════╝██║██╔════╝██║     ██╔══██╗
    █████╗  ██║█████╗  ██║     ██║  ██║
    ██╔══╝  ██║██╔══╝  ██║     ██║  ██║
    ██║     ██║███████╗███████╗██████╔╝
    ╚═╝     ╚═╝╚══════╝╚══════╝╚═════╝ 
    """)
    print(f"    [ ACTIVANDO PORTAL CLOUD ]{RESET}\n")

def banner_3rrv():
    """Banner grande para 3RRV."""
    print(f"{RED}")
    print(r"""
    ██████╗ ██████╗ ██████╗ ██╗   ██╗
    ╚════██╗██╔══██╗██╔══██╗██║   ██║
     █████╔╝██████╔╝██████╔╝██║   ██║
     ╚═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██████╔╝██║  ██║██║  ██║ ╚████╔╝ 
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  
    """)
    print(f"    [ INICIANDO FHXV2 SCANNER ]{RESET}\n")

def animacion_carga(color_barra):
    """Simula la barra de carga de 10 segundos con el color del módulo."""
    print(f"{WHITE}  [!] ESTABLECIENDO CONEXIÓN SEGURA...")
    for i in range(1, 11):
        porcentaje = i * 10
        barra = "█" * i + "░" * (10 - i)
        print(f"\r  {color_barra}[{barra}] {porcentaje}% - Descargando paquetes... {RESET}", end="")
        time.sleep(1)
    print(f"\n\n  {WHITE}[+] ENLACE ESTABLECIDO.{RESET}\n")
    time.sleep(0.5)

def ejecutar_en_cmd(tipo):
    """Lanza el CMD con el color y script correspondiente."""
    ps_base = "powershell -NoProfile -ExecutionPolicy Bypass -Command \"IEX (Invoke-RestMethod '{url}')\""

    if tipo == "FIELD":
        url_target = "https://raw.githubusercontent.com/XwwwhoIAmL/FIELD-CLOUD/refs/heads/main/FIELD%20CLOUD.ps1"
        portal = "http://googleusercontent.com/immersive_entry_chip/0"
        webbrowser.open(portal)
        cmd_final = f"color 0b & title FIELD CLOUD ACTIVE & {ps_base.format(url=url_target)}"
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/k {cmd_final}", None, 1)

    elif tipo == "3RRV":
        url_target = "https://raw.githubusercontent.com/XwwwhoIAmL/fhx-checker/refs/heads/main/FHXV2.ps1"
        cmd_final = f"color 0c & title 3RRV FHXV2 SCANNER & {ps_base.format(url=url_target)}"
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/k {cmd_final}", None, 1)

def main():
    if os.name == 'nt': os.system('color')
    rtr_banner()
    
    print(f"{WHITE}  [ SELECCIONE UN PROTOCOLO ]{RESET}")
    print(f"{CYAN}  1. FIELD CLOUD{RESET}")
    print(f"{RED}  2. 3RRV CHECKER (FHXV2){RESET}")
    print(f"{WHITE}  3. EJECUCIÓN SIMULTÁNEA{RESET}")
    
    opcion = input(f"\n{BLUE}  RTR > {RESET}")

    if opcion == "1":
        os.system('cls')
        banner_field_cloud()
        animacion_carga(CYAN)
        ejecutar_en_cmd("FIELD")
    
    elif opcion == "2":
        os.system('cls')
        banner_3rrv()
        animacion_carga(RED)
        ejecutar_en_cmd("3RRV")
        
    elif opcion == "3":
        os.system('cls')
        print(f"{MAGENTA}")
        print("    [ MODO CARGA TOTAL ACTIVADO ]")
        animacion_carga(MAGENTA)
        ejecutar_en_cmd("FIELD")
        ejecutar_en_cmd("3RRV")
        
    else:
        print(f"{RED}Error de entrada.{RESET}")
        time.sleep(1)
        return main()

    print(f"\n{CYAN}  >> Inyección completada. Champagnat Surco.{RESET}")
    print(f"{WHITE}  >> Presiona ENTER para finalizar sesión.{RESET}")
    input()

if __name__ == "__main__":
    if is_admin():
        main()
    else:
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            print(f"Fallo de privilegios: {e}")
            input()