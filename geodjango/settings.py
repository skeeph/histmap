from split_settings.tools import optional, include

include(
    'components/*.py',
    optional('local_settings.py')
)
