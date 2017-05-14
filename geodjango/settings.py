from split_settings.tools import optional, include

include(
    'components/base.py',
    'components/db.py',
    'components/security.py',
    'components/api.py',
    'components/static.py',
    optional('local_settings.py')
)
