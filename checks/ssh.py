from pathlib import Path

SSH_CONFIG = Path("/etc/ssh/sshd_config")


def load_ssh_config():
    """
    Lê o arquivo sshd_config e retorna um dicionário
    contendo as diretivas encontradas.
    """

    if not SSH_CONFIG.exists():
        return None

    config = {}

    with SSH_CONFIG.open("r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            parts = line.split()

            if len(parts) < 2:
                continue

            key = parts[0].lower()
            value = " ".join(parts[1:])

            config[key] = value

    return config


def check_root_login():

    config = load_ssh_config()

    if config is None:
        return {
            "check": "SSH Root Login",
            "status": "N/A",
            "message": "OpenSSH Server não está instalado."
        }

    value = config.get("permitrootlogin")

    if value is None:
        return {
            "check": "SSH Root Login",
            "status": "INFO",
            "message": "Diretiva PermitRootLogin não encontrada."
        }

    if value.lower() == "yes":
        return {
            "check": "SSH Root Login",
            "status": "ALERTA",
            "message": "PermitRootLogin = yes"
        }

    return {
        "check": "SSH Root Login",
        "status": "OK",
        "message": f"PermitRootLogin = {value}"
    }


def check_password_authentication():

    config = load_ssh_config()

    if config is None:
        return {
            "check": "SSH Password Authentication",
            "status": "N/A",
            "message": "OpenSSH Server não está instalado."
        }

    value = config.get("passwordauthentication")

    if value is None:
        return {
            "check": "SSH Password Authentication",
            "status": "INFO",
            "message": "Diretiva PasswordAuthentication não encontrada."
        }

    if value.lower() == "yes":
        return {
            "check": "SSH Password Authentication",
            "status": "ALERTA",
            "message": "Autenticação por senha está habilitada."
        }

    return {
        "check": "SSH Password Authentication",
        "status": "OK",
        "message": "Autenticação por senha desabilitada."
    }

