import redis

# Параметры redis
redis_host = '127.0.0.1'
redis_port = 6379
password = 'c7cc0f6b7129d446e70e4b225d4be5ca'
db = 1
message_body = 'sms_to_79222222222'
r = redis.StrictRedis(host=redis_host, port=redis_port, db=db, password=password, socket_timeout=None,
                      connection_pool=None, charset='utf-8', errors='strict', unix_socket_path=None)

def test_redis_communication():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, db=db, password=password, decode_responses=True)
        message = r.get(message_body)
        a = r.delete('sms_ip_limiter_94_242_133_146')  # чтобы понятнее
        b = r.delete('change_phone_94_242_133_146')
        c = r.delete('sms_to_79222222222')
        print("\n Очищаем redis, чтобы не получить бан\n-----------------------\n"+" Отображаю результаты удаления "
              +"(если 1 - удалил, если 0 - не было никаких данных):\n",
              "\n Лимит SMS = "+str(a),"\n Смена номера = "+str(b),"\n Количество SMS на указанный номер = "+str(c))
    except Exception as e:
        print(e)