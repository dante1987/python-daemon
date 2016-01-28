from maxwell import MaxwellDaemon, PIDFILE, WORKDIR, STDOUT

if __name__ == '__main__':
    demon = MaxwellDaemon(pidfile=PIDFILE, workdir=WORKDIR, stdout=STDOUT)
    demon.stop()
    print('Stopped the demon!!')
