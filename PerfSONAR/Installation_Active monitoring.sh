### Ubuntu 16
cd /etc/apt/sources.list.d/
wget http://downloads.perfsonar.net/debian/perfsonar-jessie-release.list
wget -qO - http://downloads.perfsonar.net/debian/perfsonar-debian-official.gpg.key | apt-key add -

apt-get install perfsonar-toolkit
apt-get install unattended-upgrades
echo 'APT::Periodic::Update-Package-Lists "1";' > /etc/apt/apt.conf.d/60unattended-upgrades-perfsonar
echo 'APT::Periodic::Unattended-Upgrade "1";' >> /etc/apt/apt.conf.d/60unattended-upgrades-perfsonar
echo 'APT::Periodic::AutocleanInterval "31";' >> /etc/apt/apt.conf.d/60unattended-upgrades-perfsonar
echo 'Unattended-Upgrade::Origins-Pattern:: "origin=perfSONAR";' >> /etc/apt/apt.conf.d/60unattended-upgrades-perfsonar

/usr/lib/perfsonar/scripts/service_watcher

service pscheduler-scheduler start
service pscheduler-runner start
service pscheduler-archiver start
service pscheduler-ticker start
service owamp-server start
service bwctl-server start
service perfsonar-lsregistrationdaemon start
