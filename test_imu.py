from machine import I2C, Pin
import time
from imu import MPU6050
from fusion import Fusion

i2c = I2C(1, sda=Pin(18), scl=Pin(19), freq=10000)
imu = MPU6050(i2c)
fuse = Fusion()

count = 0
while True:
    fuse.update_nomag(imu.accel.xyz, imu.gyro.xyz)
    if count % 5 == 0:
        print("Pitch, Roll: {:7.3f} {:7.3f}".format(
            fuse.pitch,
            fuse.roll))
    time.sleep_ms(20)
    count += 1
