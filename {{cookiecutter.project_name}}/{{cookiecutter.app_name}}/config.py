import os
from enum import Enum

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig:
    """
    Development configuration presets.
    """
    DEBUG = True
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig:
    """
    Testing configuration presets.
    """
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True


class ProductionConfig:
    """
    Testing configuration presets.
    """
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True


class ConfigurationType(Enum):
    DEVELOPMENT = DevelopmentConfig
    TESTING = TestingConfig
    PRODUCTION = ProductionConfig
