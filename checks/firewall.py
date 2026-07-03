import shutil
import subprocess


def check_firewall():

    #
    # UFW
    #

    if shutil.which("ufw"):

        try:

            result = subprocess.run(
                ["ufw", "status"],
                capture_output=True,
                text=True,
                timeout=5
            )

            output = result.stdout.lower()

            if "status: active" in output:

                return {
                    "check": "Firewall",
                    "status": "OK",
                    "message": "UFW está ativo."
                }

            return {
                "check": "Firewall",
                "status": "ALERTA",
                "message": "UFW instalado, porém desativado."
            }

        except Exception as e:

            return {
                "check": "Firewall",
                "status": "ERRO",
                "message": str(e)
            }

    #
    # firewalld
    #

    if shutil.which("firewall-cmd"):

        try:

            result = subprocess.run(
                ["firewall-cmd", "--state"],
                capture_output=True,
                text=True,
                timeout=5
            )

            output = result.stdout.lower()

            if "running" in output:

                return {
                    "check": "Firewall",
                    "status": "OK",
                    "message": "firewalld está ativo."
                }

            return {
                "check": "Firewall",
                "status": "ALERTA",
                "message": "firewalld instalado, porém parado."
            }

        except Exception as e:

            return {
                "check": "Firewall",
                "status": "ERRO",
                "message": str(e)
            }

    return {
        "check": "Firewall",
        "status": "N/A",
        "message": "Nenhum firewall suportado encontrado."
    }

