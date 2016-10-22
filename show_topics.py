#!/usr/bin/env python2

from kafka import KafkaConsumer
from pprint import pprint
import argparse

parser = argparse.ArgumentParser(description="Show server topics.")
parser.add_argument("-s", type=str, default="localhost",
                    help="Server (default: localhost)")
parser.add_argument("-p", type=str, default="9092",
                    help="Port (default: 9092)")

args = parser.parse_args()

parsed_server = "{}:{}".format(args.s, args.p)

consumer = KafkaConsumer(bootstrap_servers=[parsed_server])
pprint(consumer.topics())
