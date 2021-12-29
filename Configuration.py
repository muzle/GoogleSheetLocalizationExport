# Data for program management
class Configuration:
    def __init__(self):
        # The path to the file that you received after completing the second step.
        self.clientSecretPath = None
        # The path to the directory where the result of the program execution will be placed.
        self.destinationPath = None
        # URL address of your GoogleSheetTable.
        self.sheetUrl = None
        # The name of GoogleSheet, for example `List1`.
        self.sheetKey = None
        # Column index of the module in your GoogleSheetTable.
        self.moduleColumn = 0
        # Column index of the key in your GoogleSheetTable.
        self.keyColumn = 1
        # Column index of the comment in your GoogleSheetTable.
        self.commentColumn = 2
        # Column index of the locale in your GoogleSheetTable.
        self.localeColumn = 3
        # Row index of the language type in your GoogleSheetTable.
        self.languageRow = 1
        # Row index of the first entry of the module.
        self.contentRow = 2

    # Initialization from the dictionary
    def set(self, initial_data):
        for key in initial_data:
            setattr(self, key, initial_data[key])
