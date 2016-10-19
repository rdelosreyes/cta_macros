from examples.calibration_pipeline import display_telescope
from ctapipe.utils.datasets import get_path
import pickle, gzip
import argparse
from matplotlib import pyplot as plt

def main():
    parser = argparse.ArgumentParser(
        description='Display each event in the file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--file', dest='input_file', action='store',
                        default=get_path('gamma_test.simtel.gz'),
                        help='path to the input file')
    parser.add_argument('-t', '--telescope', dest='tel', action='store',
                        type=int, default=None,
                        help='telecope to view. Default = All')
    parser.add_argument('-D', dest='display', action='store_true',
                        default=False, help='display the camera events')
    parser.add_argument('--pdf', dest='output_path', action='store',
                        default=None,
                        help='path to store a pdf output of the plots')

    args, excess_args = parser.parse_known_args()

    #geom_dict = {}

    with gzip.open(args.input_file,"rb") as f:
        geom_dict = pickle.load(f)
        container = pickle.load(f)
    

    fig = plt.figure(figsize=(16, 7))
    if args.display:
        plt.show(block=False)
    pp = PdfPages(args.output_path) if args.output_path is not None else None

    print(geom_dict)
    for event in container:
        print(event.dl1.run_id,event.dl1.event_id)
        display_telescope(event, args.tel, args.display, geom_dict, pp, fig)

    f.close()
    
if __name__ == '__main__':
    main() 
