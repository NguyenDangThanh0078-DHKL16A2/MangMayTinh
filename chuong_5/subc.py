import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc): 
    if rc == 0:
        print("Kết nối thành công")
    else:
        print("Kết nối thất bại với mã lỗi: " + str(rc))

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_start()
