import pyflight.status
import csv
import sys
import time


def wait():
    time.sleep(30)

if __name__ == '__main__':
    writer = None
    tracker = pyflight.status.FlightInfo()

    while True:
        try:
            status = tracker.gogoinflight_metadata()
        except pyflight.status.NoFlightDataException, fde:
            print 'err %s getting flight data: %s' % (fde.__class__.__name__, str(fde))
            wait()
            continue

        if writer is None:
            fh = open(sys.argv[1], 'w')
            writer = csv.DictWriter(fh, list(status.keys()), extrasaction='ignore')
            writer.writeheader()

        writer.writerow(status)
        fh.flush()
        print 'lat=%0.6f lon=%0.6f' % (status['latitude'], status['longitude'])

        wait()
