#/usr/bin/env python3

import rclpy
from rclpy.node import Node

class TestNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info("nodo creado")

def main(args = None):
    rclpy.init(args=args)
    node = TestNode('test_node')
    rclpy.spin(node)
    rclpy.shutdown()