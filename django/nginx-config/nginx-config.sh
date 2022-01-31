#!/bin/bash
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
pip install -r requirements.txt
pip install gunicorn
sudo apt install nginx

user=$(whoami)

project_name=$(pwd | grep -o '[^/]*$')
echo $project_name
echo $user
python3 nginx-config/config.py $user $project_name
service_file_name="${project_name}.service"
nginx_file_name="${project_name}"
socket_file_name="${project_name}.socket"
echo $service_file_name
echo $nginx_file_name
echo $socket_file_name
sudo cp "nginx-config/$socket_file_name" "/etc/systemd/system/gunicorn.socket"
sudo cp "nginx-config/$service_file_name" "/etc/systemd/system/gunicorn.service"
sudo systemctl daemon-reload
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo cp "nginx-config/$nginx_file_name" "/etc/nginx/sites-available/$project_name"
sudo ln -s "/etc/nginx/sites-available/$nginx_file_name" "/etc/nginx/sites-enabled/"
sudo systemctl restart nginx
sudo systemctl restart gunicorn