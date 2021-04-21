useradd docker
mkdir /home/docker
mkdir /opt/logs 
mkdir /opt/ml
mkdir app
mkdir app/py
touch app/__init__.py
chown docker:docker /home/docker
addgroup docker staff
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen

apt-get clean
apt-get update -y
apt-get install -y curl uvicorn libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6