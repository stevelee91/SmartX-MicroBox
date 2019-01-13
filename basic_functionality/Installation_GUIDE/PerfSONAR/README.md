# Active monitoring

## 1. Installation for Active monitoring (Auto Updates enabled)

## 2. Configuration file
## 3.Central Management (MaDDash) for viewing

http://103.22.221.55/maddash-webui/


### Run PerfSONAr
 /etc/init.d/maddash-server restart

### mesh file on web
/var/www/html/mesh.json

### mesh file on perfsonar

vi /etc/perfsonar/meshconfig-agent.conf 

### LOGS
/var/log/perfsonar/meshconfig-agent.log 

### maddash configuration file location

Configuration

### Command to publish mesh file as json

/usr/lib/perfsonar/bin/build_json -o /var/www/mesh.json mesh.conf

### yaml file template

https://github.com/esnet/esnet-perfsonar-mesh/edit/master/maddash/maddash.yaml.template



