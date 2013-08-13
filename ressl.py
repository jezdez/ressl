import os
from importd import d

__version__ = '0.2'

d(
    DEBUG='RESSL_DEBUG' in os.environ,
    INSTALLED_APPS=['djangosecure'],
    MIDDLEWARE_CLASSES=['djangosecure.middleware.SecurityMiddleware'],
    SECURE_SSL_REDIRECT=True,
    SECURE_PROXY_SSL_HEADER=(
        os.environ.get('RESSL_PROXY_PROTOCOL', 'HTTP_X_FORWARDED_PROTOCOL'),
        'https'
    ),
    ALLOWED_HOSTS=[
        host.strip()
        for host in os.environ.get('RESSL_ALLOWED_HOSTS', '').split(',')
    ],
)

# just for gunicorn
application = d

if __name__ == "__main__":
    d.main()
