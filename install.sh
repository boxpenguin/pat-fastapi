# What needs to be done.
# clone github project to /opt/
# run as root
# ignore cross OS distro differences with a simple "detect debian/systemd only"
# Copy  pat-fastapi.service to /etc/systemd/system/

cd /opt/pat-fastapi

cp ./pat-fastapi.service /etc/systemd/system/
chown root:root /etc/systemd/system/pat-fastapi.service
chmod 644 /etc/systemd/system/pat-fastapi.service

touch /var/log/pat-fastapi.log
chmod 744 /var/log/pat-fastapi.log
chown root:root /var/log/pat-fastapi.log

systemctl daemon-reload
systemctl start pat-fastapi.service
systemctl enable pat-fastapi.service