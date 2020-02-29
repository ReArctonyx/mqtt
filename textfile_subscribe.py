# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# import re (regular expression) untuk filter
import re

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    # filter pesan yang masuk 
    match = re.match('AAA', str(message.payload.decode("utf-8")))

    #jika ada pola AAA tulis ke result_a.txt
    if match:
        with open("text_a.txt","a+") as data_a:
            data_a.write(str(message.payload.decode("utf-8"))+'\n')
        
    # lainnya tulis ke result_b.txt
    else:
        with open("text_b.txt","a+") as data_b:
            data_b.write(str(message.payload.decode("utf-8"))+'\n')
    
########################################
    
# buat definisi nama broker yang akan digunakan
broker_address = '192.168.0.4'

# buat client baru bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("connecting to broker")
client.connect(broker_address,port=1883)

# jalankan loop client
client.loop_start()

# client melakukan subsribe ke topik 1 dan topik 2
print("Subscribing to topic")
client.subscribe("topik_1")
client.subscribe("topik_2")

# loop forever
while True:
    # berikan waktu tunggu 1 detik 
    time.sleep(1)

#stop loop
client.loop_stop()
