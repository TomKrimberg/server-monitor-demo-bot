class BotError(Exception):
    """Base class for other exceptions"""
    pass

class ConfigurationError(BotError):
    """Invalid token or settings"""
    pass
class DemoDataError(BotError):
    """Raised when demo data is invalid"""
    pass
class FormattingError(BotError):
    """Formatting failed"""
    pass