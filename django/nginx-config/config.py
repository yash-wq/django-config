
import os
import sys
env_name = input("Enter the name of the virtual environment: ")
domain = input("Enter the domain you have configured to the IP: ")
user = sys.argv[1]
project_name = sys.argv[2]

# socket file for gunicorn
socket_file_contents = """
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
"""
with open(f"nginx-config/{project_name}.socket", 'w') as f:
    f.write(socket_file_contents)
print("socket file done")
# service file for gunicorn
service_file_contents = f"""
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User={user}
Group=www-data
WorkingDirectory=/home/{user}/{project_name}
ExecStart=/home/{user}/{project_name}/{env_name}/bin/gunicorn \
          --access-logfile - \
          --workers 1 \
          --bind unix:/run/gunicorn.sock \
          {project_name}.wsgi:application

[Install]
WantedBy=multi-user.target
"""
with open(f"nginx-config/{project_name}.service", 'w') as f:
    f.write(service_file_contents)

# Nginx file
nginx_file_contents = """
server {
    listen 80;
    server_name """ + domain + """ ;

    location = /favicon.ico {access_log off; log_not_found off; }
    location /static/ {
        root /home/"""+user+"/"+project_name+""";
}
 location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
"""
with open(f"nginx-config/{project_name}", 'w') as f:
    f.write(nginx_file_contents)
