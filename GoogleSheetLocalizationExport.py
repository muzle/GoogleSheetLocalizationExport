import sys
from yamlSupport.YamlConfigurationSupport import YamlConfigurationSupport
from googleSheetSupport.GoogleSheetSupport import GoogleSheetSupport
from iosSupport.iOSLocalizationSettings import iOSLocalizationSettings


def log_menu():
    menu = """commands:\n1. cnfg - create default localization.yml\n2. fetch - fetch localization"""
    print(menu)


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        log_menu()
    elif args[1] == "cnfg":
        YamlConfigurationSupport.create_default()
    elif args[1] == "fetch":
        config = YamlConfigurationSupport.get_config()
        localizations = GoogleSheetSupport.get_localizations()
        iOSLocalizationSettings.create(localizations, config)
    else:
        log_menu()
