cgroup_memory_text_exporter
=========

This role installs a timer with a program that scrapes cgroup info from filesystem and dumps into node_exporter textfile format output.

Requirements
------------

You'll need node_exporter.

Role Variables
--------------

`node_exporter_textfile_dir`, defaults to `/var/lib/node_exporter`

Dependencies
------------

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
