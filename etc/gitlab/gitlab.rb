registry_external_url 'https://gitlab.com:5555'
registry_nginx['ssl_certificate'] = "/etc/letsencrypt/live/gitlab.com/fullchain.pem"
registry_nginx['ssl_certificate_key'] = "/etc/letsencrypt/live/gitlab.com/privkey.pem"