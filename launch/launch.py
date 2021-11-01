from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    ld = LaunchDescription()

    publisher_node = Node(
        package = "py_pubsub",
        executable = "publisher",
    )

    subscriber_node = Node(
        package = "py_pubsub",
        executable = "subscriber",
    )

    ld.add_action(publisher_node)
    ld.add_action(subscriber_node)

    return ld
