import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 5060))
    s.listen()
    print("სერვერი ელოდება კლიენტს...")
    conn, addr = s.accept()

    with conn as conn:
        data = conn.recv(1024).decode("utf-8")
        print("მივიღეთ:", data)
        upper_data = data.upper()
        conn.sendall(upper_data.encode("utf-8"))

