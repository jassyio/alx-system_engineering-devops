#!/usr/bin/env bash
# Install nginx and add a custom header
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
echo "Holberton School" > /var/www/html/index.nginx-debian.html
echo "Ceci n'est pas une page" > /usr/share/nginx/html/custom_404.html
sed -i "/listen 80 default_server/a \\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default
sed -i "/listen 80 default_server/a \\\terror_page 404 /custom_404.html; location = /custom_404.html {root /usr/share/nginx/html;\n\tinternal;}" /etc/nginx/sites-available/default
sed -i "/listen 80 default_server/a \\\tadd_header X-Served-By $(hostname);" /etc/nginx/sites-available/default
service nginx restart