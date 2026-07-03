from checks.ssh import (
    check_root_login,
    check_password_authentication,
)

from checks.firewall import check_firewall

def print_result(result):

    print(f"[{result['status']:^6}] {result['check']}")
    print(f"        {result['message']}\n")


def main():

    print("=" * 60)
    print("SecureConfigAudit")
    print("=" * 60)
    print()

    checks = [
        check_root_login,
        check_password_authentication,
	check_firewall,
    ]

    for check in checks:
        print_result(check())


if __name__ == "__main__":
    main()

