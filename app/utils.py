# todo:
# checar questão de encriptar o token

from typing import List, Dict, Any


def organize_contacts_by_domain(
    data: Dict[str, Any]
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Organiza contatos por domínio de e-mail de forma otimizada.

    Args:
        data (dict): Dicionário contendo a lista de contatos.

    Returns:
        dict: Lista de domínios com seus respectivos contatos.
    """
    contacts_by_domain = {}

    for contact in data.get("connections", []):
        if "emailAddresses" in contact and "names" in contact:
            email_info = contact["emailAddresses"][0]
            name_info = contact["names"][0]

            email = email_info.get("value")
            name = name_info.get("displayName")

            if email and name:
                domain = email.split("@")[-1].strip().lower()

                if domain not in contacts_by_domain:
                    contacts_by_domain[domain] = []

                contacts_by_domain[domain].append({"name": name, "email": email})

    return [
        {"domain": domain, "emails": emails}
        for domain, emails in contacts_by_domain.items()
    ]
