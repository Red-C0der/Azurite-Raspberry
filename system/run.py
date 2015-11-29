# -*- coding: utf-8 -*-
__author__ = 'Red_C0der'

#   /=============================================================================\
#  |   ██████╗ ███████╗██████╗          ██████╗ ██████╗ ██████╗ ███████╗██████╗    |
#  |   ██╔══██╗██╔════╝██╔══██╗        ██╔════╝██╔═████╗██╔══██╗██╔════╝██╔══██╗   |
#  |   ██████╔╝█████╗  ██║  ██║        ██║     ██║██╔██║██║  ██║█████╗  ██████╔╝   |
#  |   ██╔══██╗██╔══╝  ██║  ██║        ██║     ████╔╝██║██║  ██║██╔══╝  ██╔══██╗   |
#  |   ██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║   |
#  |                                                                               |
#  |   Project-Name: Azurite                                                       |
#  |   Version: 0.0.2                                                              |
#  |   Development-State: Alpha                                                    |
#  |   Project-ID: 0777                                                            |
#  |   GitHub-Page: https://github.com/Red-C0der/Azurite-Raspberry                 |
#  |   License: /LICENSE.txt                                                       |
#  |                                                                               |
#  |                                                                               |
#  |   Personal-Info:                                                              |
#  |   Twitter: https://twitter.com/red_c0der                                      |
#  |   FaceBook: -                                                                 |
#  |   E-Mail: redc0der.mail@gmail.com                                             |
#   \=============================================================================/

debug = 1

try:
    import logger
    import output
    lloc = "File: run.py | Message: "
    logger.write("i", "Starting Boot!", lloc=lloc)
    output.statePrint("ok", "Successfully imported logger and output !", debug=debug)
    logger.write("i", "Successfully imported logger and output !", lloc=lloc)
    output.statePrint("", "Importing socket", debug=debug)
    import socket
    output.statePrint("ok", "Successfully imported socket !", debug=debug)
    logger.write("i", "Successfully imported socket !", lloc=lloc)
    output.statePrint("", "Importing asyncore", debug=debug)
    import asyncore
    output.statePrint("ok", "Successfully imported asyncore !", debug=debug)
    logger.write("i", "Successfully imported asyncore !", lloc=lloc)
    output.statePrint("", "Importing time", debug=debug)
    import time
    output.statePrint("ok", "Successfully imported time !", debug=debug)
    logger.write("i", "Successfully imported time !", lloc=lloc)
    output.statePrint("", "Importing cryptographer as crypto", debug=debug)
    import cryptographer as crypto
    output.statePrint("ok", "Successfully imported cryptographer as crypto !", debug=debug)
    logger.write("i", "Successfully imported cryptographer as crypto !", lloc=lloc)
    output.statePrint("", "Importing configparser as cfg", debug=debug)
    import configparser as cfg
    output.statePrint("ok", "Successfully imported configparser as cfg !", debug=debug)
    logger.write("i", "Successfully imported configparser as cfg !", lloc=lloc)
    output.statePrint("", "Importing sys", debug=debug)
    import sys
    output.statePrint("ok", "Successfully imported sys !", debug=debug)
    logger.write("i", "Successfully imported sys !", lloc=lloc)
except ImportError:
    try:
        output.statePrint("error", "Could not import specific module! Quitting system!", debug=debug)
        logger.write("e", "Could not import specific module! Quitting system!", lloc=lloc)
        sys.exit(0)
    except:
        print "ERROR: Could not import specific module! Quitting system!"
        logger.write("e", "Could not import specific module! Quitting system!", lloc=lloc)
        sys.exit(0)

try:
    output.statePrint("", "Getting Machine IP Address, Hostname, and socket-networking port!", debug=debug)
    logger.write("i", "Getting Machine IP Address, Hostname, TrustedHosts and ports!", lloc=lloc)
    hostname = cfg.getattrib("network/myhostname", "val", debug=debug)
    output.statePrint("ok", "Got hostname! ["+str(hostname)+"]", debug=debug)
    logger.write("i", "Got hostname! ["+str(hostname)+"]", lloc=lloc)
    myip = cfg.getattrib("network/ips/myhost", "val", debug=debug)
    output.statePrint("ok", "Got myip! ["+str(myip)+"]", debug=debug)
    logger.write("i", "Got myip! ["+str(myip)+"]", lloc=lloc)
    ports = cfg.getelementlist("network/ports/port", debug=debug)
    output.statePrint("ok", "Got ports!", debug=debug)
    logger.write("i", "Got ports!", lloc=lloc)
    trustedhosts = cfg.getelementlist("trustedhosts/host", debug=debug)
    output.statePrint("ok", "Got Trustedhosts!", debug=debug)
    logger.write("i", "Got Trustedhosts!", lloc=lloc)
    print trustedhosts

    output.statePrint("", "Getting socket-networking port from ports !", debug=debug)
    logger.write("i", "Getting socket-networking port from ports !", lloc=lloc)
    for port in ports:
        if port["usage"] == "socket":
            socketport = port["port"]
            output.statePrint("ok", "Got socket-networking port! ["+str(socketport)+"]", debug=debug)
            logger.write("i", "Got socket-networking port! ["+str(socketport)+"]", lloc=lloc)
    if not socketport:
        output.statePrint("error", "Could not get socket-networking port! Quitting system!", debug=debug)
        logger.write("e", "Could not get socket-networking port! Quitting system!", lloc=lloc)
        sys.exit(0)
except:
    output.statePrint("error", "Some error in block 2!", debug=debug)
    logger.write("e", "Some error occoured in block 2!", lloc=lloc)
    sys.exit(0)

try:
    output.statePrint("", "Doing some class creation!", debug=debug)
    logger.write("i", "Doing some class creation!")
except:
    output.statePrint("error", "Some error in block 3!", debug=debug)
    logger.write("e", "Some error occoured in block 3!", lloc=lloc)

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self):
        lloc = "File: run.py | Class: EchoServer | Function: __init__ | Message: "
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        logger.write("i", "Created Socket Object!", lloc=lloc)
        self.set_reuse_addr()
        self.bind((str(myip), int(socketport)))
        logger.write("i", "Bound socket to ip ["+str(myip)+"] port ["+str(socketport)+"]!", lloc=lloc)
        maxconnections = 1
        self.listen(maxconnections)
        logger.write("i", "Socket is now listening for ["+str(maxconnections)+"] connections!", lloc=lloc)

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            pass
        else:
            sock, addr = pair
            for host in trustedhosts:
                if host["ip"] == addr:
                    if int(host["level"]) > 6:
                        output.statePrint("info", "Received verified incoming connection from [%s]!" % repr(addr), debug=debug)
                        logger.write("i", "Received verified incoming connection from [%s]!" % repr(addr), lloc=lloc)
                    elif int(host["level"]) < 6:
                        output.statePrint("warning", "Received unverified incoming connection from [%s]!" % repr(addr), debug=debug)
                        logger.write("w", "Received unverified incoming connection from [%s]!" % repr(addr), lloc=lloc)
            handler = EchoHandler(sock)


try:
    output.statePrint("", "Starting socket server with ip and port! ["+str(myip)+"] & ["+str(socketport)+"]", debug=debug)
    logger.write("i", "Starting socket server with ip and port! ["+str(myip)+"] & ["+str(socketport)+"]", lloc=lloc)
    server = EchoServer()
    output.statePrint("ok", "Successfully started socket server with ip and port! ["+str(myip)+"] & ["+str(socketport)+"]", debug=debug)
    logger.write("i", "Successfully started socket server with ip and port! ["+str(myip)+"] & ["+str(socketport)+"]", lloc=lloc)
    output.statePrint("info", "Please connect to ip ["+str(myip)+"] from the Main Azurite Machine!", debug=debug)
    logger.write("i", "Please connect to ip ["+str(myip)+"] from the Main Azurite Machine!", lloc=lloc)
except:
    output.statePrint("error", "Some error while starting socket server!", debug=debug)
    logger.write("e", "Some error while starting socket server!", lloc=lloc)
    sys.exit(0)

i = 0
while True:
    print "RUNNING LELELELE"
    print i
    i = i + 1
    time.sleep(0.5)
    #i = raw_input("root$ ")
    #print "Input: " + i
#asyncore.loop()
