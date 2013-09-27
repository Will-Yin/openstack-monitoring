openstack monitoring with centreon/nagios/ndoutils/mysql
========================================================


##nagios nrpe config on the hosts

#This is the remote host service configuration 

#Base on all the hosts
###################################################################

command[check_users]=/usr/lib/nagios/plugins/check_users -w 20 -c 30
command[check_load]=/usr/lib/nagios/plugins/check_load -w 15,10,5 -c 30,20,10
command[check_zombie_procs]=/usr/lib/nagios/plugins/check_procs -w 5 -c 10 -s Z
command[check_total_procs]=/usr/lib/nagios/plugins/check_procs -w 500 -c 800
command[check_swap]=/usr/lib/nagios/plugins/check_swap -w '50%' -c '25%'
command[check_mem]=/usr/lib/nagios/plugins/check_mem.sh -w 250 -c 150 -p
command[check_chef_client]=/usr/lib/nagios/plugins/check_procs -w 1:2 -c 1:2 -C ruby -a chef-client
command[check_smtp]=/usr/lib/nagios/plugins/check_smtp -H
command[check_local_time]=/usr/lib/nagios/plugins/check_ntp_time -H 127.0.0.1
command[check_ntp]=/usr/lib/nagios/plugins/check_ntp -H 127.0.0.1
#SSH
command[check_ssh]=/usr/lib/nagios/plugins/check_ssh -H 127.0.0.1 -t 10
#Disk
command[check_disk]=/usr/lib/nagios/plugins/check_disk -w 15% -c 10% -p /


#Cinder surely controller
##########################################################################
command[check_port_cinder-api]=/usr/lib/nagios/plugins/check_tcp -H  127.0.0.1 -p 8776
command[check_cinder-api-proc]=/usr/lib/nagios/plugins/check_procs -w 1:2 -c 2:10 -a "cinder-api"
command[check_cinder-scheduler-proc]=/usr/lib/nagios/plugins/check_procs -w 1:2 -c 2:10 -a "cinder-scheduler"
command[check_cinder-volume-proc]=/usr/lib/nagios/plugins/check_procs -w 2:2 -c 2:10 -a "cinder-volume"

#Glance surely controller
#########################################################################
command[check_glance-api]=/usr/lib/nagios/plugins/check_procs -w 2:10 -c 1:100 -a "glance-api"
command[check_glance-registry]=/usr/lib/nagios/plugins/check_procs -w 2:10 -c 1:100 -a "glance-registry"
command[check_port_glance-registry]=/usr/lib/nagios/plugins/check_tcp -H x.x.x.x -p 9191
command[check_port_glance-api]=/usr/lib/nagios/plugins/check_tcp -H x.x.x.x -p 9292

#Keystone
########################################################################
command[check_keystone]=/usr/lib/nagios/plugins/check_procs -w 2:10 -c 1:100 -a "keystone"
command[check_port_keystone-admin]=/usr/lib/nagios/plugins/check_tcp -H x.x.x.x -p 35357
command[check_port_keystone-service]=/usr/lib/nagios/plugins/check_tcp -H x.x.x.x -p 5000

#Horizon Dashboard - Controller
########################################################################
command[check_nova_dashboard-server]=/usr/lib/nagios/plugins/check_procs -w 2:10 -c 1:100 -a "nova_dashboard-server"
command[check_port_nova_dashboard-server]=/usr/lib/nagios/plugins/check_tcp -H 127.0.0.1 -p 80

#nova - part Controller - part compute 
#########################################################################
command[check_nova_mysql]=/usr/lib/nagios/plugins/check_mysql -H localhost -u nova -p bvm53mg73eud -d nova
command[check_nova_manage]=sudo /usr/lib/nagios/plugins/check_nova_manage -S 1 -N 1 -C 2 -w 1 -c 3
command[check_nova_api]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "nova-api"
command[check_nova_compute]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "nova-compute"
command[check_nova_network]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "nova-network"
command[check_nova_scheduler]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "nova-scheduler"

#Quantum - Networking
#########################################################################

command[check_quantum_openvswitch_agent]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "quantum-openvswitch-agent"
command[check_quantum-server]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "quantum-server"
command[check_quantum-metadata-agent]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "quantum-metadata-agent"
command[check_quantum-dhcp-agent]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "quantum-dhcp-agent"
command[check_quantum-l3-agent]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "quantum-l3-agent"
command[check_port_quantum-service]=/usr/lib/nagios/plugins/check_tcp -H x.x.x.x -p 9696

#rabbitMQ - Controller
##########################################################################
command[check_rabbit]=/usr/lib/nagios/plugins/check_rabbitmq_aliveness -H x.x.x.x -u nova -p shs4evy7k85x --vhost /nova
#queue depth. I need to find the tresholds for warning and critical
command[check_rabbitmq_overview]=/usr/lib/nagios/plugins/check_rabbitmq_overview  -H x.x.x.x -u nova -p shs4evy7k85x
#rabbitMQ server - This is very good in cluster situation which we will have in production.
command[check_rabbitmq_server]=/usr/lib/nagios/plugins/check_rabbitmq_server  -H x.x.x.x -u nova -p shs4evy7k85x -n


#OVS - Compute and network
##########################################################################
#ovsdb-server
command[check_ovsdb_server]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "ovsdb-server"
#ovs-vswitchd
command[check_ovs_vswitchd]=/usr/lib/nagios/plugins/check_procs -w 2:4 -c 2:10 -a "ovs-vswitchd"

#libvirtd - Compute
command[check_libvirtd]=/usr/lib/nagios/plugins/check_procs -w 1:2 -c 2:10 -a "libvirtd"

#Mysql Server - Will become percona and utilize the percona plugins
##########################################################################
command[check_mysql_server]=/usr/lib/nagios/plugins/check_mysql -H localhost -u debian-sys-maint -p mvyy37d3cjwk


#Apache Proc - Controller
##########################################################################
command[check_apache]=/usr/lib/nagios/plugins/check_procs -w 1:10 -c 2:10 -a "apache2"
