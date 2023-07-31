install_requirements:
	pip3 install --upgrade --force-reinstall --no-cache-dir -r requirements.txt

run:
	sudo python3 qrcode-generator.py

# just run if needed
update:
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade setuptools
