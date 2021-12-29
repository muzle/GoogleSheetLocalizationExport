import ruamel.yaml
from Configuration import Configuration


class YamlConfigurationSupport:
    __FileName = 'localization.yml'
    __ConfigurationFieldName = 'Configuration'

    @staticmethod
    def get_config():
        with open(YamlConfigurationSupport.__FileName, 'r') as stream:
            yaml = ruamel.yaml.YAML()
            data = yaml.load(stream)
            configuration = Configuration()
            configuration.set(data[YamlConfigurationSupport.__ConfigurationFieldName])
            return configuration

    @staticmethod
    def write_config(configuration):
        with open(YamlConfigurationSupport.__FileName, 'w') as yamlFile:
            yaml_str = YamlConfigurationSupport.__create_yaml_config(configuration)
            yaml = ruamel.yaml.YAML()
            code = yaml.load(yaml_str)
            yaml.dump(code, yamlFile)

    @staticmethod
    def create_default():
        YamlConfigurationSupport.write_config(Configuration())

    @staticmethod
    def __create_yaml_config(configuration):
        return '''\
        {0}:
# The path to the file that you received after completing the second step.
            clientSecretPath: {1}
# The path to the directory where the result of the program execution will be placed.
            destinationPath: {2}
# URL address of your GoogleSheetTable.
            sheetUrl: {3}
# The name of GoogleSheet, for example `List1`.
            sheetKey: {4}
# Column index of the module in your GoogleSheetTable.
            moduleColumn: {5}
# Column index of the key in your GoogleSheetTable.
            keyColumn: {6}
# Column index of the comment in your GoogleSheetTable.
            commentColumn: {7}
# Column index of the locale in your GoogleSheetTable.
            localeColumn: {8}
# Row index of the language type in your GoogleSheetTable.
            languageRow: {9}
# Row index of the first entry of the module.
            contentRow: {10}
        '''.format(YamlConfigurationSupport.__ConfigurationFieldName, configuration.clientSecretPath,
                   configuration.destinationPath,  configuration.sheetUrl, configuration.sheetKey,
                   configuration.moduleColumn, configuration.keyColumn, configuration.commentColumn,
                   configuration.localeColumn, configuration.languageRow, configuration.contentRow
                   )
