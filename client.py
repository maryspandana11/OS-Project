import xmlrpc.client
import random
import time

proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

def perform_random_operation():
    operation = random.choice(["magicAdd", "magicSubtract", "magicFindMin", "magicFindMax"])
    if operation == "magicAdd" or operation == "magicSubtract":
        a = random.uniform(1, 100)
        b = random.uniform(1, 100)
        result = getattr(proxy, operation)(a, b)
    elif operation == "magicFindMin" or operation == "magicFindMax":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        result = getattr(proxy, operation)(a, b, c)
    print(f"[Client] {operation} result: {result}")
    return result

def generate_requests(num_requests=1000):
    for _ in range(num_requests):
        perform_random_operation()

def get_server_counts():
    counts = proxy.get_counts()
    print("\n[Client] Server operation counts:")
    for op, count in counts.items():
        print(f"{op}: {count}")

if __name__ == "__main__":
    generate_requests(1000)
    get_server_counts()
