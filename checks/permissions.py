from pathlib import Path
import stat


def check_file_permission(file_path, expected_mode):
    """
    Verifica se um arquivo possui a permissão esperada.
    """

    path = Path(file_path)

    if not path.exists():
        return {
            "check": f"Permissões de {file_path}",
            "status": "ERRO",
            "message": "Arquivo não encontrado."
        }

    try:
        current_mode = stat.S_IMODE(path.stat().st_mode)

        if current_mode == expected_mode:
            return {
                "check": f"Permissões de {file_path}",
                "status": "OK",
                "message": f"Permissões corretas ({oct(current_mode)})"
            }

        return {
            "check": f"Permissões de {file_path}",
            "status": "ALERTA",
            "message": (
                f"Permissões atuais: {oct(current_mode)} "
                f"(esperado: {oct(expected_mode)})"
            )
        }

    except Exception as e:
        return {
            "check": f"Permissões de {file_path}",
            "status": "ERRO",
            "message": str(e)
        }


def check_passwd_permissions():
    return check_file_permission("/etc/passwd", 0o644)


def check_shadow_permissions():
    return check_file_permission("/etc/shadow", 0o640)


def check_sudoers_permissions():
    return check_file_permission("/etc/sudoers", 0o440)

