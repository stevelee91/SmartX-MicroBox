This docker script installs the perfsonar-toolkit and perfsonar-centralmanagement. Installation is based on the latest centos6 build. Before you start you'll need to install docker.

In debian this can be done with the following commands:

apt-get update

apt-get install -y apt-transport-https ca-certificates

apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

echo 'deb https://apt.dockerproject.org/repo debian-jessie main' > /etc/apt/sources.list.d/docker.list

apt-get update

apt-cache policy docker-engine

apt-get install -y docker-engine

service docker start

And test if docker works...:

docker run hello-world

Also make sure that ntp is running on the host:

apt-get install ntp

/etc/init.d/ntp start

ntpq -p

To install this perfsonar docker image do the following:

git clone https://github.com/MigielDV/perfsonar.git

cd perfsonar

Make sure you edit the lsregistrationdaemon.conf file such that it matches your needs.

docker build -t perfsonar .

docker run --privileged -P --net=host -v /var/run -i -t perfsonar

To run the container in the background use the -d (detached) flag or press CTRL-p + CTRL-q.
