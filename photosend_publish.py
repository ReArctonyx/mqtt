# import paho
import paho.mqtt.client as mqtt

# definsi broker yang digunakan
broker_address = 'localhost'

# buat client bernama P1
print("creating new instance")
client = mqtt.Client("P1")

# client terkoneksi ke broker
print("connecting to broker")
client.connect(broker_address,port=1883)

# print "baca file"
print ("read file")

# buka file surf.jpg
with open("surf-man.jpg","rb") as img:

# baca semua isi file
    read_data = img.read()

# ubah file dalam bentuk byte gunakan fungsi byte()
    file = bytes(read_data)

# publish dengan topik photo dan data dipublish adalah file
print("publish foto")
client.publish("photo",file)

# client loop mulai
client.loop_start()

# tutup file
img.close()
