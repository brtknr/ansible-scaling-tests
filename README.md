# Ansible Scaling Tests

Generate inventory:

	./inventory.py --ini 100 > inventory.ini

Run playbook:

	ansible-playbook -i inventory.ini playbook.yml
