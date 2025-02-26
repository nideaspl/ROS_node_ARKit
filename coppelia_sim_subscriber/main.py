import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class ARCoordinateSubscriber(Node):
    def __init__(self):
        super().__init__('ar_coordinate_subscriber')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'ar_coordinates',
            self.listener_callback,
            10)
        self.subscription  # Prevent unused variable warning

    def listener_callback(self, msg):
        coordinates = msg.data
        print(f"Received coordinates in CoppeliaSim: {coordinates}")
        # Here you can use a remote API to move objects in CoppeliaSim

def main(args=None):
    rclpy.init(args=args)
    node = ARCoordinateSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

