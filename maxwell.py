import sys
import time
import datetime
from demon import Daemon


PIDFILE = '/users/krzysztofskarupa/Desktop/pid.pid'
WORKDIR = '/users/krzysztofskarupa/Desktop/'
STDOUT = '/users/krzysztofskarupa/Desktop/stdout.txt'


class MaxwellDaemon(Daemon):

    date_file = '/users/krzysztofskarupa/Desktop/plik.txt'

    def run(self):
        print('zaczynam')
        while True:
            print('bla')
            time.sleep(3)
            with open(self.date_file, 'a') as fil:
                fil.write(datetime.datetime.now().strftime("%D %H:%M:%S\n"))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You need to give argument: start or stop')
        sys.exit(0)

    demon = MaxwellDaemon(pidfile=PIDFILE, workdir=WORKDIR, stdout=STDOUT)

    if sys.argv[1] == 'start':
        demon.start()
    elif sys.argv[1] == 'stop':
        demon.stop()
    else:
        print('wrong argument')
