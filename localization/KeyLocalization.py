class KeyLocalization:
    def __init__(self, key, comment, translations):
        # The key by which the desired translation will be found
        self.key = key
        # Translation comment
        self.comment = comment
        # An array of all possible translations of the text, translation index must be equal to language index
        self.translations = translations
