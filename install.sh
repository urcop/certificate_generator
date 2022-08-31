echo "Запуск установки нужных компонентов"
sudo apt install docker docker-compose -y
sudo apt install python3.8-venv

echo "Запуск питона со всеми нужными компонентами"
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
docker run --name sirius_db -e POSTGRES_PASSWORD=siriusconnect -e POSTGRES_USER=anna -e POSTGRES_DB=sirius_db -p 999:5432 -d postgres && docker start sirius_db
