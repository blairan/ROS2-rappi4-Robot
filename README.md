# ROS2-rappi4-Robot
this repository is base on Raspiberry

## Project

### 1.Nodes
- Publisher
- Subscriber

### 2.test_pwm_1.py(gpio_pin_test)
> note
> see this error "PermissionError: [Errno 13] Permission denied: '/dev/i2c-1'"  to do.. \
$ sudo chown blairan /dev/i2c-1 \
$ sudo chmod g+rw /dev/i2c-1
