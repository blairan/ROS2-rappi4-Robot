#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.pub = self.create_publisher(String, "chatter", 10) 
        self.c = 0 
        self.create_timer(0.5, self.callback) 

    def callback(self): 
        msg=String() 
        msg.data="hello world" 
        self.pub.publish(msg) 
        self.c +=1 
        self.get_logger().info(f"publish: {msg.data} {str(self.c)}") 
        
def main(args=None): 
    rclpy.init(args=args) 
    node = PublisherNode("publish_node") 
    rclpy.spin(node) 
    rclpy.shutdown() 

if __name__=="__main__":
    main()