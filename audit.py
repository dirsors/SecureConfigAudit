from checks.ssh import (
    check_root_login,
    check_password_authentication,
)

from checks.firewall import check_firewall

from checks.permissions import (
    check_passwd_permissions,
    check_shadow_permissions,
    check_sudoers_permissions,
)


def print_result(result):
    print(f"[{result['status']:^6}] {result['check']}")
    print(f"        {result['message']}\n")


def calculate_score(results):

    score = 100

    for result in results:

        status = result["status"]

        if status == "ALERTA":
            score -= 15

        elif status == "ERRO":
            score -= 20

        elif status == "N/A":
            score -= 5

    if score < 0:
        score = 0

    return score


def classify_score(score):

    if score >= 90:
        return "EXCELENTE"

    elif score >= 75:
        return "BOM"

    elif score >= 60:
        return "REGULAR"

    elif score >= 40:
        return "RUIM"

    return "CRÍTICO"


def main():

    checks = [
        check_root_login,
        check_password_authentication,
        check_firewall,
        check_passwd_permissions,
        check_shadow_permissions,
        check_sudoers_permissions,
    ]

    results = []

    print("=" * 60)
    print("SecureConfigAudit")
    print("=" * 60)
    print()

    for check in checks:

        result = check()

        results.append(result)

        print_result(result)

    #
    # Resumo
    #

    total = len(results)

    ok = sum(r["status"] == "OK" for r in results)
    alert = sum(r["status"] == "ALERTA" for r in results)
    error = sum(r["status"] == "ERRO" for r in results)
    info = sum(r["status"] == "INFO" for r in results)
    na = sum(r["status"] == "N/A" for r in results)

    score = calculate_score(results)

    classification = classify_score(score)

    print("=" * 60)
    print("Resumo da Auditoria")
    print("=" * 60)

    print(f"Verificações executadas : {total}")
    print(f"OK                      : {ok}")
    print(f"ALERTA                 : {alert}")
    print(f"ERRO                   : {error}")
    print(f"INFO                   : {info}")
    print(f"N/A                    : {na}")
    print()

    print(f"Pontuação de Segurança : {score}/100")
    print(f"Classificação          : {classification}")


if __name__ == "__main__":
    main()
