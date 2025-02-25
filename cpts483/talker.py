from cpts483_interfaces.srv import Reply

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(Reply, 'talk2human', self.talk2human_callback)

    def talk2human_callback(self, request, response):
        self.get_logger().info('Incoming request: %s' % (request.question))
        if (request.question in ["Hello!", "hello", "Hi", "Hello", "Hi!"]):
            response.answer = "Hello, Human!"
        else:
            response.answer = "Sorry, I do not understand. "

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
