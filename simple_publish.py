# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
import datetime

#callback : fungsi yang akan dipanggil jika message di buffer
#####################
def on_publish(client, userdata, message):
    print("message received" ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
######################

# definisikan nama broker yang akan digunakan
broker_address = 'localhost'

# buat client baru bernama P2
print("creating new instance")
client = mqtt.Client("P2")

#client.on_publish=on_publish
client.on_publish = on_publish
# koneksi ke broker
print("connecting to broker")
client.connect(broker_address,port=1883)

# mulai loop client
client.loop_start()

# lakukan 20x publish waktu dengan topik 1
print("publish something")
for i in range (20):
    # sleep 1 detik
    time.sleep(1)
    # publish waktu sekarang
    print("Publishing current time")
    client.publish("waktu",str(datetime.datetime.now()))

#stop loop
client.loop_stop()