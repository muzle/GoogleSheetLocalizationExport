import pygsheets
from yamlSupport.YamlConfigurationSupport import YamlConfigurationSupport
from localization.KeyLocalization import KeyLocalization
from localization.ModuleLocalization import ModuleLocalization
from localization.FullLocalization import FullLocalization


class GoogleSheetSupport:
    @staticmethod
    def get_localizations():
        config = YamlConfigurationSupport.get_config()
        GoogleSheetSupport.__check_config(config)
        service = pygsheets.authorize(config.clientSecretPath)
        sheets = service.open_by_url(config.sheetUrl)
        if config.sheetKey is None:
            sheet = sheets.sheet1
        else:
            sheet = sheets.worksheet_by_title(config.sheetKey)

        all_values = sheet.get_all_values()
        all_languages_array = [string for string in all_values[config.languageRow] if string != ""]
        languages_array = []

        for index in range(config.localeColumn, len(all_languages_array)):
            language = all_languages_array[index]
            if language:
                languages_array.append(language)

        dict = {}
        module = ""
        for index in range(config.contentRow, len(all_values)):
            line = all_values[index]
            if len(line[config.moduleColumn]) != 0:
                module = line[config.moduleColumn]
            if len(line[config.keyColumn]) == 0:
                continue
            translations = []
            for index in range(config.localeColumn, (config.localeColumn + len(languages_array))):
                translations.append(line[index])
            key_localization = KeyLocalization(line[config.keyColumn], line[config.commentColumn], translations)
            try:
                dict[module].append(key_localization)
            except KeyError:
                dict[module] = [key_localization]

        modules = []
        for key in dict.keys():
            modules.append(ModuleLocalization(key, dict[key]))

        return FullLocalization(modules, languages_array)

    @staticmethod
    def __check_config(config):
        if config.clientSecretPath is None:
            raise Exception('Empty account access file path')
        if config.sheetUrl is None:
            raise Exception('Empty sheet url')
        if config.localeColumn is None:
            raise Exception('Empty locale column')
        if config.languageRow is None:
            raise Exception('Empty locale row')
        if config.moduleColumn is None:
            raise Exception('Empty module column')
        if config.keyColumn is None:
            raise Exception('Empty key column')
        if config.commentColumn is None:
            raise Exception('Empty comment column')
