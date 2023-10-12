# test_API_service

# install docker and python
<pre>
sudo apt update
sudo apt install docker-compose python3
</pre>

# download project
git clone https://github.com/graffwinterfield/test_API_service.git\n
cd test_API_service/\n
pip install -r requirments.txt

# start
python3 main.py
![image](https://github.com/graffwinterfield/test_API_service/assets/110451740/293e09a8-d4f1-42bd-85bb-657dca036f91)

# usage
curl -X POST -H "Content-Type: application/json" -d "{\"questions_num\": 100}" http://127.0.0.1:5000/api/generate_questions/
![image](https://github.com/graffwinterfield/test_API_service/assets/110451740/563bcfc3-7a04-4504-9b2c-258f90133540)

# manage Database
http://127.0.0.1:5000/admin
![image](https://github.com/graffwinterfield/test_API_service/assets/110451740/1df3a95a-53ff-4516-ba44-2b884c099a30)

python3 test.py - test for check request time
![image](https://github.com/graffwinterfield/test_API_service/assets/110451740/43e2c27d-304d-47ea-8cd2-e990038b4bfd)

