import os
from pathlib import Path
from iosSupport.iOSLocalizationStringsConstants import *
from iosSupport.iOSLocalizationConstants import *
import re


class iOSLocalizationSettings:
    @staticmethod
    def create(full_localization, configuration):
        iOSLocalizationSettings.__create_strings_localizations(full_localization, configuration)
        iOSLocalizationSettings.__create_localization(full_localization, configuration)

    @staticmethod
    def __create_strings_localizations(full_localization, configuration):
        destination_path = iOSLocalizationSettings.__destination_path(configuration)
        for index in range(0, len(full_localization.languages)):
            language = full_localization.languages[index]
            dir_name = DIR_NAME_MASK.format(language)
            dir_path_str = destination_path + "/" + dir_name
            dir_path = Path(dir_path_str)
            if not dir_path.exists():
                dir_path.mkdir()
            file_path = dir_path_str + "/" + FILE_NAME
            result = LOCALIZATION_HEADER_FORMAT.format(configuration.sheetUrl) + iOSLocalizationSettings.__create_strings_localization(full_localization, index)
            with open(file_path, "w") as file:
                file.write(result)

    @staticmethod
    def __create_localization(full_localization, configuration):
        file_path = iOSLocalizationSettings.__destination_path(configuration) + "/" + SWIFT_FILE_NAME
        result = LOCALIZATION_HEADER_FORMAT.format(configuration.sheetUrl) + FILE_HEADER
        result += iOSLocalizationSettings.__create_localization_content(full_localization)
        result += FILE_FOOTER
        with open(file_path, "w") as file:
            file.write(result)

    @staticmethod
    def __create_strings_localization(full_localization, language_id):
        result = ""
        for module in full_localization.modules:
            for key in module.keys:
                if len(key.comment) > 0:
                    result += LOCALIZATION_COMMENT_FORMAT.format(key.comment)
                result += LOCALIZATION_FORMAT.format(module.module, key.key, key.translations[language_id])
        return result

    @staticmethod
    def __create_localization_content(full_localization):
        result = ""
        compile = re.compile(r'\%([0-9]+)\@')
        for module in full_localization.modules:
            if module != full_localization.modules[0]:
                result += "\n"
            result += MODULE_HEADER.format(module.module)
            for key in module.keys:
                if len(key.translations) > 0:
                    result += KEY_COMMENT.format(key.translations[0])
                    translation_parameters_indexes = compile.findall(key.translations[0])
                    if len(translation_parameters_indexes) > 0:
                        all = list(set(translation_parameters_indexes))
                        sorted(all)
                        parameters = ""
                        body = KEY_FUNCTION_BODY_START.format(module.module, key.key)
                        for value in all:
                            parameters += KEY_FUNCTION_PARAMETER.format(value)
                            body += KEY_FUNCTION_BODY_ELEMENT.format(value)
                            if value != all[-1]:
                                parameters += ", "
                                body += ", "
                        body += KEY_FUNCTION_BODY_FINISH
                        result += KEY_FUNCTION_HEADER.format(parameters)
                        result += body
                        result += KEY_FUNCTION_FOOTER
                    else:
                        result += KEY_VALUE.format(module.module, key.key)
            result += MODULE_FOOTER
        return result

    @staticmethod
    def __destination_path(configuration):
        path_str = os.getcwd()
        if configuration.destinationPath is not None:
            path_str += configuration.destinationPath
        path = Path(os.path.normpath(path_str))
        if not path.exists():
            raise Exception('invalid destination path')

        par_dir_path_str = path_str + "/GoogleSheetLocalization/"
        par_dir_path = Path(par_dir_path_str)
        if not par_dir_path.exists():
            par_dir_path.mkdir()
        return par_dir_path_str
