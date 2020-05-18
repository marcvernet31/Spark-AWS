#!/bin/bash

#usage: ./automatic_deployment.sh path_to_aws_key ip1 ip2 .... ipn

keypath=$1
shift

for ip in $@; do
   ssh -o StrictHostKeyChecking=no -i $keypath ubuntu@$ip 'sudo apt-get update; sudo apt-get install python -y; sudo apt-get install python-pip -y; pip install nltk==3.4.1; sudo apt-get install openjdk-8-jre -y; wget http://archive.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz; tar xvfz spark-2.4.3-bin-hadoop2.7.tgz; rm -f spark-2.4.3-bin-hadoop2.7.tgz; ssh-keygen -t rsa -N "" -f .ssh/id_rsa; sudo apt-get install python-pip; sudo pip install nltk'
   scp -i $keypath ubuntu@$ip:./.ssh/id_rsa.pub $ip.txt
done

rm -f slaves authorized

for ip in $@; do
   echo $ip >> slaves
   cat $ip.txt >> authorized
done

for ip in $@; do
   scp -i $keypath slaves ubuntu@$ip:./spark-2.4.3-bin-hadoop2.7/conf/
   scp -i $keypath authorized ubuntu@$ip:.
   ssh -i $keypath ubuntu@$ip 'cat authorized >> .ssh/authorized_keys'
   rm -f $ip.txt
done

rm -f slaves
rm -f authorized


