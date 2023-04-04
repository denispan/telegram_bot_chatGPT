Телеграм-бот на основе chatGPT







Deploy на сервер

создаем папку виртуального окружения
python3 -m venv venv

активируем виртуальное окружение
source venv/bin/activate

устанавливаем нужные пакеты
pip3 install -r requirements.txt

создаем скрин для бота с именем
screen -S bot_wo_db

запускаем бота
python3 main.py
