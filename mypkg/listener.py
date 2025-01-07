# SPDX-FileCopyrightText: 2025 Rin Hanaoka <s23c1110vk@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class MemoryListener(Node):
    def __init__(self):
        super().__init__("memory_listener")
        self.create_subscription(Float64, "memory_usage", self.listener_callback, 10)

    def listener_callback(self,msg):
        self.get_logger().info(f'Memory Usage {msg.data} %')

def main():
    rclpy.init()
    node = MemoryListener()
    rclpy.spin(node)
