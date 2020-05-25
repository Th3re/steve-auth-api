from api.app import contacts_manager


def get(userId):
    contacts = contacts_manager.get_contacts(userId)
    return {
        "contacts": contacts
    }
