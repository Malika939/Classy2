class ContactList(list):
    def search_by_name(self, name):
        result = []
        for i in self:
            if i == name:
                result.append(i)
        return result


all_contacts = ContactList()
all_contacts += ['Vasya', 'Petya', 'Erbol', 'Nurdoolot', 'Apolinarij']
all_contacts.append('Vasya')
print(all_contacts)
print(all_contacts.search_by_name('Vasya'))