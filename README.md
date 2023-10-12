﻿# test_API_service

# install docker and python
sudo apt update
sudo apt install docker-compose python3

# download project
git clone https://github.com/graffwinterfield/test_API_service.git
cd test_API_service/
pip install -r requirments.txt

#start
python3 main.py

#usage
curl -X POST -H "Content-Type: application/json" -d "{\"questions_num\": 100}" http://127.0.0.1:5000/api/generate_questions/

python3 test.py - test for check request time
