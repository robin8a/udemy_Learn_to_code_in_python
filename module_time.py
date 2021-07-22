import time as t
time_now = t.localtime()
epoch_time = t.time()
print ( "Type: " , type (time_now) )
print ( "Hour: " + str (t.localtime().tm_hour) )
print ( "Epoch: " + str (epoch_time) )

delivery_time = epoch_time + ( 86400 *7 )

print ("Delivery time (7 days)", t.localtime(delivery_time) )


t.sleep(5)

print ("Wait 5 seconds")



