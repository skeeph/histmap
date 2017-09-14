import os

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAdminUser',
    # ],
    'PAGE_SIZE': os.environ.get("PAGE_SIZE",20)
}
