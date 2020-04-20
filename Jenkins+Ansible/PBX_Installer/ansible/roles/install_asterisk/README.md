Installing Asterisk
=========
'''
---
- name: Install Asterisk for Centos 7
  hosts: "{{ units }}"

  roles:
    - { role: install_asterisk, when: ansible_distribution == 'CentOS' }
'''
need vars:

unit: name
