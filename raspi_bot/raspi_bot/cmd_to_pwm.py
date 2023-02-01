import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
sys.path.append('/home/blairan/ros2_ws/src/ROS2-rappi4-Robot/raspi_bot')
from scripts.BOARD import DFRobot_Expansion_Board_IIC as Board
from scripts.mygpio import mygpio
import RPi.GPIO as GPIO
import time

class cmd_to_pwm_driver(Node, Board):
    def __init__(self):
        super().__init__("cmd_vel_sub")
        self.board = Board(1, 0x10)
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
        self.board_detect()
        while self.board.begin() != self.board.STA_OK:    # Board begin and check board status
            self.print_board_status()
            print("board begin faild")
            time.sleep(2)
            print("board begin success")
        self.board.set_pwm_enable()  # Pwm channel need external power
        # board.set_pwm_disable()
        self.board.set_pwm_frequency(1000) # Set frequency to 1000HZ, Attention: PWM voltage depends on independent power supply
        time.sleep(1)
        print("set part pwm all channels duty to 60%")
        # self.board.set_pwm_duty(self.board.ALL, 60)
        time.sleep(1)
        self.board.set_pwm_duty(0, 60) # Set pwm0 channels duty
        self.board.set_pwm_duty(1, 60)  # Set pwm1 channels duty
        self.board.set_pwm_duty(2, 60)  # Set pwm2 channels duty
        self.board.set_pwm_duty(3, 60)  # Set pwm3 channels duty
        time.sleep(1)

        self.create_subscription(Twist, "cmd_vel", self.cmd_vel_pwm_callback, 10)
        

    def cmd_vel_pwm_callback(self, msg):
        right_wheel_vel = (msg.linear.x + msg.angular.z)/2
        left_wheel_vel = (msg.linear.x - msg.angular.z)/2

        print(left_wheel_vel,"/",right_wheel_vel)


        if left_wheel_vel > 0 and right_wheel_vel > 0:
            GPIO.output(8,GPIO.HIGH)#left 1(0)
            GPIO.output(9,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)#left 2(1)
            GPIO.output(7,GPIO.HIGH)

            GPIO.output(10,GPIO.LOW)#right 1(2)
            GPIO.output(11,GPIO.HIGH)
            GPIO.output(4,GPIO.HIGH)#right 2(3)
            GPIO.output(5,GPIO.LOW)
            print("forward")

        elif left_wheel_vel < 0 and right_wheel_vel < 0:
            GPIO.output(8,GPIO.LOW)#left 1(0)
            GPIO.output(9,GPIO.HIGH)
            GPIO.output(6,GPIO.HIGH)#left 2(1)
            GPIO.output(7,GPIO.LOW)

            GPIO.output(10,GPIO.HIGH)#right 1(2)
            GPIO.output(11,GPIO.LOW)
            GPIO.output(4,GPIO.LOW)#right 2(3)
            GPIO.output(5,GPIO.HIGH)
            print("backup")
        
        elif left_wheel_vel < 0 and right_wheel_vel > 0:
            GPIO.output(8,GPIO.LOW)#left 1(0)
            GPIO.output(9,GPIO.HIGH)
            GPIO.output(6,GPIO.HIGH)#left 2(1)
            GPIO.output(7,GPIO.LOW)

            GPIO.output(10,GPIO.LOW)#right 1(2)
            GPIO.output(11,GPIO.HIGH)
            GPIO.output(4,GPIO.HIGH)#right 2(3)
            GPIO.output(5,GPIO.LOW)
            print("left")


        elif left_wheel_vel > 0 and right_wheel_vel < 0:
            GPIO.output(8,GPIO.HIGH)#left 1(0)
            GPIO.output(9,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)#left 2(1)
            GPIO.output(7,GPIO.HIGH)

            GPIO.output(10,GPIO.HIGH)#right 1(2)
            GPIO.output(11,GPIO.LOW)
            GPIO.output(4,GPIO.LOW)#right 2(3)
            GPIO.output(5,GPIO.HIGH)
            print("right")
        
            
        else:
            GPIO.output(8,GPIO.LOW)#left 1(0)
            GPIO.output(9,GPIO.LOW)
            GPIO.output(6,GPIO.LOW)#left 2(1)
            GPIO.output(7,GPIO.LOW)

            GPIO.output(10,GPIO.LOW)#right 1(2)
            GPIO.output(11,GPIO.LOW)
            GPIO.output(4,GPIO.LOW)#right 2(3)
            GPIO.output(5,GPIO.LOW)
            
    

    def board_detect(self):
        l = self.board.detecte()
        print("Board list conform:")
        print(l)

    ''' print last operate status, users can use this variable to determine the result of a function call. '''
    def print_board_status(self):
        if self.board.last_operate_status == self.board.STA_OK:
            print("board status: everything ok")
        elif self.board.last_operate_status == self.board.STA_ERR:
            print("board status: unexpected error")
        elif self.board.last_operate_status == self.board.STA_ERR_DEVICE_NOT_DETECTED:
            print("board status: device not detected")
        elif self.board.last_operate_status == self.board.STA_ERR_PARAMETER:
            print("board status: parameter error")
        elif self.board.last_operate_status == self.board.STA_ERR_SOFT_VERSION:
            print("board status: unsupport board framware version")



def main(args=None):
    rclpy.init(args=args)
    node=cmd_to_pwm_driver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__name__":
    main()
