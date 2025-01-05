# SPDX-FileCopyrightText: 2025 Rin Hanaoka <s23c1110vk@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import psutil

class MemoryPublisher(Node):
    def __init__(self):
        super().__init__('memory_publisher')
        self.pub = self.create_publisher(Float64, 'memory_usage', 10)
        self.create_timer(1.0, self.publish_memory_usage)

    def publish_memory_usage(self):
        memory_usage_value = psutil.virtual_memory().percent
        msg = Float64()
        msg.data = memory_usage_value
        self.pub.publish(msg)
        self.get_logger().info(f'Memory Usage: {memory_usage_value}%')
        
def main():
    rclpy.init()
    node = MemoryPublisher()
    rclpy.spin(node)