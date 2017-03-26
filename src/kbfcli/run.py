"""Process desired command, parse arguments and execute desired action"""

import logging
import argparse
from .config import KBFConfig, KBFConfigError


def run(args):
    """Parse arguments and dispatch actions"""
    logging.basicConfig()
    parser = argparse.ArgumentParser(description="CLI for KanbanFlow (www.kanbanflow.com)")
    parser.add_argument('--config', type=KBFConfig, help="Path to configuration file")

    try:
        parser.parse_args(args)
    except KBFConfigError:
        logging.fatal("Invalid config file")
        return 1
