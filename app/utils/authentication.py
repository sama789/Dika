'''
Class for Authentication, her Constructor has two Parameters uid and mail
 with the Function authenticated User to know who has been loggin
'''


class AuthenticatedUser:

    def __init__(self, uid, mail):
        self.uid = uid
        self.mail = mail


# Fake Date (SSO)
def get_authenticated_user(): 
    return AuthenticatedUser('samah', "samah.munawwer@tuhh.de")
    # return AuthenticatedUser("ha", "ha@gmail.com")
    # return AuthenticatedUser("Xuser", "sam@gmail.com")
