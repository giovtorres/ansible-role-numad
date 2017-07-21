Ansible Role: numad
===================

Installs and configures numad, a system daemon that monitors NUMA topology.
This role also installs the numactl and numastat utilities.  Supported on EL 6
and 7.

Requirements
------------

numad is useful on systems with two or more NUMA nodes.  See numad(8).

Role Variables
--------------

Set the time interval that numad waits between system scans (seconds):

    numad_interval: 15

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - giovtorres.numad

License
-------

BSD
