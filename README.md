Телеграм-бот на основе chatGPT
#
</br>

Deploy на сервер</br>
</br>
создаем папку виртуального окружения</br>
python3 -m venv venv</br>
</br>
активируем виртуальное окружение</br>
source venv/bin/activate</br>
</br>
устанавливаем нужные пакеты</br>
pip3 install -r requirements.txt</br>
</br>
создаем скрин для бота с именем</br>
screen -S bot_wo_db</br>
</br>
запускаем бота</br>
python3 main.py</br>
