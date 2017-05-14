# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/gstatic/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'npm.finders.NpmFinder'
]

STATIC_ROOT = "gstatic"

NPM_FILE_PATTERNS = {
    'leaflet': ['dist/*'],
    'bootstrap': ['dist/*']

}