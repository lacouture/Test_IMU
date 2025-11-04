#! /usr/bin/env sh

mpremote fs cp micropython-mpu9x50/imu.py      :/lib/
mpremote fs cp micropython-mpy9x50/vector3d.py :/lib/

mpremote fs cp micropython-fusion/deltat.py    :/lib/
mpremote fs cp micropython-fusion/fusion.py    :/lib/

mpremote fs cp test_imu.py                     :/
