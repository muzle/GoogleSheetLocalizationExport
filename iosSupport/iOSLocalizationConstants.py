SWIFT_FILE_NAME = u'GSln.generated.swift'
FILE_HEADER = u"""import Foundation

// swiftlint:disable superfluous_disable_command file_length implicit_return

// MARK: - Strings

// swiftlint:disable explicit_type_interface function_parameter_count identifier_name line_length
// swiftlint:disable nesting type_body_length type_name vertical_whitespace_opening_braces
internal enum GSln {
"""
FILE_FOOTER = u"""
}
// swiftlint:enable explicit_type_interface function_parameter_count identifier_name line_length
// swiftlint:enable nesting type_body_length type_name vertical_whitespace_opening_braces

// MARK: - Implementation Details

extension GSln {
  private static func tr(_ table: String, _ key: String, _ args: CVarArg...) -> String {
    let format = BundleToken.bundle.localizedString(forKey: key, value: nil, table: table)
    return String(format: format, locale: Locale.current, arguments: args)
  }
}

// swiftlint:disable convenience_type
private final class BundleToken {
  static let bundle: Bundle = {
    #if SWIFT_PACKAGE
    return Bundle.module
    #else
    return Bundle(for: BundleToken.self)
    #endif
  }()
}
// swiftlint:enable convenience_type
"""
MODULE_HEADER = u'\tinternal enum {0} {{'
MODULE_FOOTER = u'\n\t}'
KEY_COMMENT = u'\n\t\t/// {0}'
KEY_VALUE = u'\n\t\tinternal static let {1} = GSln.tr("GSln", "{0}.{1}")'

KEY_FUNCTION_HEADER = u'\n\t\tinternal static func cantOpenApp({0}) -> String {{'
KEY_FUNCTION_PARAMETER = u'_ p{0}: Any'
KEY_FUNCTION_BODY_START = u'\n\t\t\treturn GSln.tr("GSln", "{0}.{1}", '
KEY_FUNCTION_BODY_ELEMENT = u'String(describing: p{0})'
KEY_FUNCTION_BODY_FINISH = u')'
KEY_FUNCTION_FOOTER = u'\n\t\t}'