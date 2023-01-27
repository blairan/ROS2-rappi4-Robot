import rclpy #ROS2接口
from  rclpy.node import Node 
from std_msgs.msg import String 

class SubscriberNode(Node):

    def __init__(self, name): 
        super().__init__(name)
        self.c = 0
        self.sub = self.create_subscription( 
            String, "chatter", self.callback, 10)
        
    def callback(self, msg): 
        msg = String()
        msg.data = "hello world"
        self.c += 1 
        self.get_logger().info(f"i heard : {msg.data} {str(self.c)}") 

def main(args=None): 
    rclpy.init(args=args) 
    node = SubscriberNode("subscriber_node") 
    rclpy.spin(node) 
    rclpy.shutdown() 

if __name__=="__main__":
    main()