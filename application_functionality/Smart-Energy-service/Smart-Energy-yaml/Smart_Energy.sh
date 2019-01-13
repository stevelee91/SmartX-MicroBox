#!/bin/bash


#chmod 777 /home/ubuntu/Smart-Energy-Service/all_things/Smart-Energy-yaml/SmartX-EdgeX-yaml/hack/*
#cd /home/ubuntu/Smart-Energy-Service/all_things/Smart-Energy-yaml/SmartX-EdgeX-yaml
#./hack/edgex-up.sh
#cd /home/ubuntu/Smart-Energy-Service/all_things/Smart-Energy-yaml
kubectl apply -f zookeeper.yaml
kubectl apply -f kafka.yaml
kubectl apply -f influx_chro.yaml
kubectl apply -f api_server.yaml
kubectl apply -f EdgeX.yaml
#kubectl apply -f consumer_d1_inference.yaml



