# Ansible Scaling Tests

Generate inventory:

	./inventory.py --ini 100 > inventory.ini

Relax MaxStartups policy in sshd config:

	ansible-playbook sshd-config.yml

Run playbook:

	ansible-playbook -i inventory.ini playbook.yml -f 100
