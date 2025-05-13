import threading
from xmlrpc.server import SimpleXMLRPCServer
import random
import time

class MathServer:
    def __init__(self):
        self.magic_add_count = 0
        self.magic_subtract_count = 0
        self.magic_findmin_count = 0
        self.magic_findmax_count = 0
        self.lock = threading.Lock()

    def magicAdd(self, a, b):
        with self.lock:
            self.magic_add_count += 1
        print(f"[Server] magicAdd({a}, {b}) = {a + b}")
        return a + b

    def magicSubtract(self, a, b):
        with self.lock:
            self.magic_subtract_count += 1
        print(f"[Server] magicSubtract({a}, {b}) = {a - b}")
        return a - b

    def magicFindMin(self, a, b, c):
        with self.lock:
            self.magic_findmin_count += 1
        result = min(a, b, c)
        print(f"[Server] magicFindMin({a}, {b}, {c}) = {result}")
        return result

    def magicFindMax(self, a, b, c):
        with self.lock:
            self.magic_findmax_count += 1
        result = max(a, b, c)
        print(f"[Server] magicFindMax({a}, {b}, {c}) = {result}")
        return result

    def get_counts(self):
        return {
            "magicAdd": self.magic_add_count,
            "magicSubtract": self.magic_subtract_count,
            "magicFindMin": self.magic_findmin_count,
            "magicFindMax": self.magic_findmax_count
        }

def start_server():
    server = SimpleXMLRPCServer(('localhost', 8000), logRequests=True)
    server.register_instance(MathServer())
    print("Server is running on port 8000...")
    server.serve_forever()

if __name__ == "__main__":
    start_server()
