from game import Game
import argparse


def pars_arguments():
    parser = argparse.ArgumentParser(
        prog='ParsArguments',
        description='Start fireworks with arguments'
    )
    parser.add_argument('-s', '--sparks-amount-range', help='This argument is need for work range', default=None)
    return parser.parse_args()


parsed_args = pars_arguments()

spark_range = None
if parsed_args.sparks_amount_range:
    try:
        min_sparks, max_sparks = map(int, parsed_args.sparks_amount_range.split('-'))
        sparks_range = (min_sparks, max_sparks)
    except ValueError:
        print("You gave me don't correct values")


if __name__ == '__main__':
    application = Game(sparks_range=spark_range)
    application.run()
