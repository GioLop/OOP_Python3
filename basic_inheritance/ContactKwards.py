class ContactList(list):
    def search(self, name):
        ''' Returns all contacts that contain the search value in their name. '''
        matching_contacts = []
        
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name='', email='', **kwargs):
        # super.__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class AddresHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super.__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send "
                "{} order to {}".format(order, self.name))

class Friend(Contact, AddresHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add email logic here
    
class EmailableContact(Contact, MailSender):
    pass