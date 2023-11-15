class Category:

    def __init__(self,id, name, description):
        self._id = id
        self._name = name
        self._description = description

    def getName(self):
        return self._name