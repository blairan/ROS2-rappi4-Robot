import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan
from cv_bridge import CvBridge
import cv2

class lidar_camera_sub(Node):
    def __init__(self):
        super().__init__("qr_maze_node")
        
        self.create_subscription(Image, "/raspi_bot_camera/image_raw", self.camera_cb, 10)
        self.create_subscription(LaserScan, "/scan", self.lidar_cb, 10)
        self.bridge=CvBridge()
        self.frame=0

    def camera_cb(self, data):
        self.frame=self.bridge.imgmsg_to_cv2(data, 'bgr8')
        cv2.imshow("frame", self.frame)
        cv2.waitKey(1)

    def lidar_cb(self, data):
        front_ray=min(data.ranges[180], 100)
        if (front_ray<=0.57):
            self.qr_detector()
        else:
            print(f"Forward")
    
    def qr_detector(self):
        detector=cv2.QRCodeDetector()
        data, point, _=detector.detectAndDecode(self.frame)
        print(data)


    
def main(args=None):
    rclpy.init(args=args)
    lidar_sensor=lidar_camera_sub()
    rclpy.spin(lidar_sensor)
    lidar_sensor.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()

