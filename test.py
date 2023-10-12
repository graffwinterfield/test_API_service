import time, requests

count = 10
for i in range(5):
    count += 200
    t1 = time.time()
    url = f'http://localhost:5000/api/generate_questions/'
    headers = {"Content-Type": "application/json"}
    data = {"questions_num": count}
    r = requests.post(url=url, headers=headers, json=data)
    t2 = time.time()
    print(f'test {i} time: {t2 - t1} requests: {count}\n answer:{r.json()}')

'''test 0 time: 3.80336594581604 requests: 30
test 1 time: 4.04764461517334 requests: 50
test 2 time: 4.421074151992798 requests: 70
test 3 time: 5.391159296035767 requests: 90
test 4 time: 5.534670114517212 requests: 110
test 5 time: 5.4253785610198975 requests: 130
test 6 time: 5.3997509479522705 requests: 150
test 7 time: 5.557071685791016 requests: 170
test 8 time: 5.462902069091797 requests: 190
test 9 time: 5.386053562164307 requests: 210

Process finished with exit code 0
'''
