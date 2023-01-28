import RPi.GPIO as GPIO
import time
from BOARD import DFRobot_Expansion_Board_IIC as Board

board = Board(1, 0x10)    # Select i2c bus 1, set address to 0x10

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

def board_detect():
    l = board.detecte()
    print("Board list conform:")
    print(l)

''' print last operate status, users can use this variable to determine the result of a function call. '''
def print_board_status():
    if board.last_operate_status == board.STA_OK:
        print("board status: everything ok")
    elif board.last_operate_status == board.STA_ERR:
        print("board status: unexpected error")
    elif board.last_operate_status == board.STA_ERR_DEVICE_NOT_DETECTED:
        print("board status: device not detected")
    elif board.last_operate_status == board.STA_ERR_PARAMETER:
        print("board status: parameter error")
    elif board.last_operate_status == board.STA_ERR_SOFT_VERSION:
        print("board status: unsupport board framware version")

def run():
    GPIO.output(8,GPIO.HIGH)#left 1(0)
    GPIO.output(9,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)#left 2(1)
    GPIO.output(7,GPIO.HIGH)

    GPIO.output(10,GPIO.LOW)#right 1(2)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(4,GPIO.HIGH)#right 2(3)
    GPIO.output(5,GPIO.LOW)
    time.sleep(1)
    GPIO.cleanup()

if __name__ == "__main__":

    board_detect()    # If you forget address you had set, use this to detected them, must have class instance

    # Set board controler address, use it carefully, reboot module to make it effective


    while board.begin() != board.STA_OK:    # Board begin and check board status
        print_board_status()
        print("board begin faild")
        time.sleep(2)
        print("board begin success")

    board.set_pwm_enable()  # Pwm channel need external power
    # board.set_pwm_disable()
    board.set_pwm_frequency(1000) # Set frequency to 1000HZ, Attention: PWM voltage depends on independent power supply
    time.sleep(1)
    print("set part pwm all channels duty to 60%")
    board.set_pwm_duty(board.ALL, 90)
    time.sleep(1)
    board.set_pwm_duty(0, 60) # Set pwm0 channels duty
    board.set_pwm_duty(1, 60)  # Set pwm1 channels duty
    board.set_pwm_duty(2, 60)  # Set pwm2 channels duty
    board.set_pwm_duty(3, 60)  # Set pwm3 channels duty
    time.sleep(1)
    run()