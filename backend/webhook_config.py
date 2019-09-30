import os

WEBHOOK_CONFS = {
    'config': {
        'url': "{}/receiver".format(os.environ.get('HOST')),
        'content_type': 'json',
        'insecure_ssl': False,
        'secret': os.environ.get('GITHUB_WEBHOOKS_SECRET'),
    },
    'events': ['push']
}
