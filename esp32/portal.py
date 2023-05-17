import network
import usocket as socket
import machine
# set the access point name and password
ap_name = "IoT_CO_Captive_portal"
ap_password = "passw0rd"



def captive_portal():
        
    # create the access point
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ap_name, password=ap_password,authmode=network.AUTH_WPA_WPA2_PSK)

    # create a socket to listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 80))
    sock.listen(1)

    # HTML content for the captive portal page
    html = """<!DOCTYPE html>
    <html>
    <head>
        <title>ESP32 Captive Portal</title>
    </head>
    <body>
        <h1>ESP32 Captive Portal</h1>
        <form method="post" action="/">
            <label for="ssid">SSID:</label>
            <input type="text" name="ssid" id="ssid"><br><br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password"><br><br>
            <input type="submit" value="Connect">
        </form>
    </body>
    </html>
    """

    # handle a client connection
    def handle_client(conn):
        print("client connected")
        request = conn.recv(1024)
        request_str = request.decode('utf-8')
        request_lines = request_str.split('\r\n')
        if len(request_lines) > 0:
            method, path, version = request_lines[0].split()
            if method == 'POST':
                content_length = int([line.split(':')[1].strip() for line in request_lines if line.startswith('Content-Length:')][0])
                data = request_str.split('\r\n\r\n')[1]
                ssid, password = [d.split('=')[1] for d in data.split('&')]
                print('New WiFi credentials: ssid={}, password={}'.format(ssid, password))
                ap.config(essid=ssid, password=password)
                #client.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body>WiFi credentials saved!</body></html>')
                print(ssid)
                print(password)
                

            # save the SSID and password to a file
                with open('wifi.txt', 'w') as f:
                    f.write(ssid + '\n' + password)
                    f.close()

            # send a response to the client
                #response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                #response += "<html><body><h1>Connected to Wi-Fi</h1></body></html>"
                #conn.send(response.encode())
                machine.reset()
                return
            # restart the ESP32 to connect to the Wi-Fi
            

            else:
            # send the captive portal page to the client
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
                response += html
                conn.send(response.encode())

            conn.close()

    # wait for client connections and handle them
    while True:
        conn, addr = sock.accept()
        handle_client(conn)
   
