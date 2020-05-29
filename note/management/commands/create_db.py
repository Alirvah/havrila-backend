import sys
import logging
import MySQLdb

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

rds_host = 'djangodb.cluster-cattl9ftli1h.eu-central-1.rds.amazonaws.com'
db_name = 'djangodb'
user_name = 'admin'
password = 'djangotestdb'
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    help = 'Creates the initial database'

    def handle(self, *args, **options):
        print('Starting db creation')
        try:
            db = MySQLdb.connect(host=rds_host, user=user_name,
                                 password=password, db="mysql", connect_timeout=5)
            c = db.cursor()
            print("connected to db server")
            c.execute("""CREATE DATABASE djangodb;""")
            c.execute(
                """GRANT ALL PRIVILEGES ON db_name.* TO 'admin' IDENTIFIED BY 'djangotestdb';""")
            c.close()
            print("closed db connection")
        except:
            logger.error(
                "ERROR: Unexpected error: Could not connect to MySql instance.")
            sys.exit()

