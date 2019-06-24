from SatTracker.sattracker import *
from SatTracker.printer import *
import datetime
import SatTracker.default as defaults
from datetime import datetime


def main():
    tracker = SatTracker()

    print("Setting ground segment Location.")
    gs_location = tracker.set_location()
    print_gs_location(gs_location)

    print("\nGetting TLE.")
    tracker.get_tle('KAZSTSAT', 'SatTracker/text_files/tle.txt')

    print("\nLoading TLE data.")
    tracker.load_tle("SatTracker\\text_files\\tle.txt")

    print("\nGround longitude/latitude under that satellite now: ")
    for i in range(10):
        sat_info = tracker.find_sat_coordinates_for_now()
        print_sat_coordinates(sat_info)
        tracker.write_statistic()
        tracker.write_sat_coordinates()
        # tracker.visualization()
        # tracker.visualization_3d_globe()
        # tracker.visualisation_mapbox()
        tracker.find_realtime_coord()
        time.sleep(5.0)
        tracker.observer.date = datetime.utcnow()

    #print("Visualization started")
    #print("Visualization finished")

    # print("Show map")
    # tracker.show_map()

    # print("\nNext passes information:")
    # for i in range(5):
    #    next_pass = tracker.next_pass()
    #    print_next_passes(next_pass)
    # tracker.find_satellite_alt_az()


# if __name__ == '__main__':
#     main()
