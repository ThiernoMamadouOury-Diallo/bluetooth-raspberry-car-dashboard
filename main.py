#!/usr/bin/env python
# coding: utf-8


"""A server that returns car dashboard informations via Bluetooth serial.

Usage:
  main.py [--speed=<kn>] [--log=<level>]
  main.py (-h | --help)
  main.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  message frequency in second.
  --log=<level> Set log level.

"""


import os
import glob
import time
import random
import time
import logging
from docopt import docopt
from bluetooth import *


def mapper_log(value):
    level = logging.ERROR
    if value == "info":
        level = logging.INFO
    elif value == "debug":
        level = logging.DEBUG
    return level

if __name__ == '__main__':

    arguments = docopt(__doc__, version='dashboardServer 0.1.0')

    logging_level = "info" if arguments['--log'] is None else arguments['--log']
    logging.basicConfig(filename="carBLE.log", format='%(asctime)s - %(levelname)s: %(message)s', level=mapper_log(logging_level))
   
    timer= float(5 if arguments['--speed'] is None else arguments['--speed'])

    server_sock = BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service( server_sock, "CarDashboard",
                    service_id = uuid,
                    service_classes = [ uuid, SERIAL_PORT_CLASS ],
                    profiles = [ SERIAL_PORT_PROFILE ], 
    #                   protocols = [ OBEX_UUID ] 
                        )

    logging.info("Waiting for connection on RFCOMM channel %d" % port)
    print("Waiting for connection on RFCOMM channel %d" % port)
    client_sock, client_info = server_sock.accept()

    logging.info("Accepted connection from %s", client_info ) 
    print("Accepted connection from %s", client_info ) 

    while True:

        try:
            req = client_sock.recv(1024)
            if len(req) == 0:
                break
            logging.info("received [%s]" % req)
            print("received [%s]" % req)

            data = None
            if req in ('1 AA-000-ZZ'):
                data = "Bienvenue a bord"
                client_sock.send(data)

            while True:
                time.sleep(timer)
                rd = random.randint(1,101) % 2
                if rd == 1:
                    data = "Niveau du carburant est de %s Litre" % str(random.randint(5,70))
                elif rd == 0:
                    data = "La temperature du moteur est de %s Celsius" % str(random.randint(10, 120))

                logging.info("sending [%s]" % data)
                print("sending [%s]" % data)
                client_sock.send(data)

        except IOError:
            pass

        except KeyboardInterrupt:

            logging.info("disconnected")
            print("disconnected")

            client_sock.close()
            server_sock.close()
            logging.info("all done")

            break


