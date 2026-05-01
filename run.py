import platform
import sys
import os
import importlib.util

C_RED = '\033[91m'
C_CYAN = '\033[96m'
C_RESET = '\033[0m'

def load_core():
    arch = platform.machine().lower()
    
    try:
        if 'aarch64' in arch or 'armv8' in arch or 'arm64' in arch:
            so_file = "core_64.so"
        elif 'armv7' in arch or 'armeabi' in arch or 'arm' in arch:
            so_file = "core_32.so"
        else:
            print(f"{C_RED}[!] Unsupported Architecture: {arch}{C_RESET}")
            sys.exit(1)

        if not os.path.exists(so_file):
            print(f"{C_RED}[!] Error: File '{so_file}' not found.{C_RESET}")
            sys.exit(1)

        spec = importlib.util.spec_from_file_location("core", so_file)
        core = importlib.util.module_from_spec(spec)
        sys.modules["core"] = core
        spec.loader.exec_module(core)

        core.main()

    except Exception as e:
        print(f"{C_RED}[!] Error: System core files are missing or incompatible.{C_RESET}")
        print(f"{C_CYAN}[Debug] Details: {e}{C_RESET}")
        sys.exit(1)

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')
    load_core()
