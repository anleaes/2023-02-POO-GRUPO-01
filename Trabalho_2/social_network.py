class SocialNetwork:

    def __init__(self, name, description):
        self._name = name
        self._description = description

    def getSocialDescription(self):
        return self._description