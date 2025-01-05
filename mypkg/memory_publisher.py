# SPDX-FileCopyrightText: 2025 Rin Hanaoka <s23c1110vk@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import psutil

class MemoryPublisher(Node):
    def __init__(self):

    def publish_memory_usage(self):
        