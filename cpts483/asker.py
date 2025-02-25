import sys

from cpts483_interfaces.srv import Reply
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(Reply, 'talk2human')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Reply.Request()

    def send_request(self, q):
        self.req.question = q
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    future = minimal_client.send_request(' '.join(sys.argv[1:]))
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()
    minimal_client.get_logger().info(
        'Result of %s: %s' %
        (' '.join(sys.argv[1:]), response.answer))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()