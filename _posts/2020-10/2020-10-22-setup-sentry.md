---
title: "Setup Sentry with Docker"
published: true
tags: Sentry
---

## Install Docker & Docker Compose

```shell
sudo yum update -y
sudo yum install docker
sudo service docker start
sudo systemctl enable docker
sudo usermod -a -G docker ec-user
# logout and check
docker-info

sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

## Install Sentry

```shell
git clone git@github.com:getsentry/onpremise.git

vim onpremise/sentry/config.yml

# change the following for Slack Integration
slack.client-id
slack.client-secret
slack.signing-secret

# in onpremise folder
dokcer-compose up -d
```

You can also configure SMTP here to enable Email invitation & notification.

## Configure Nginx

```shell
vim /etc/nginx/conf.d/snetry.conf

server {
        listen 80;
        server_name your-domain;
        location / {
            proxy_pass         https://127.0.0.1:9000;
            proxy_redirect     off;
            proxy_set_header   Host $host;
            proxy_set_header   X-Real-IP $remote_addr;
            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Host $server_name;
        }
}
```