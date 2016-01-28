from maxwell import MaxwellDaemon, PIDFILE, WORKDIR, STDOUT

if __name__ == '__main__':
    demon = MaxwellDaemon(pidfile=PIDFILE, workdir=WORKDIR, stdout=STDOUT)
    demon.start()
    print('started the demon!!')