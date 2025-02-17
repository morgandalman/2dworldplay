# broker.py - Central broker to relay messages between workers
import zmq

def run_broker():
    context = zmq.Context()

    # XSUB: Receives messages from workers
    xsub_socket = context.socket(zmq.XSUB)
    xsub_socket.bind("tcp://*:5555")

    # XPUB: Distributes messages to workers
    xpub_socket = context.socket(zmq.XPUB)
    xpub_socket.bind("tcp://*:5556")

    print("Broker running...")
    zmq.proxy(xsub_socket, xpub_socket)  # Forward messages

if __name__ == "__main__":
    run_broker()
