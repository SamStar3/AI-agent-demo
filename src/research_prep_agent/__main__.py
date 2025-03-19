"""Entry point for the Research and Preparation Agent."""

import sys
import argparse
from research_prep_agent.config.config_manager import config_manager


def main():
    """Main entry point for the Research and Preparation Agent."""
    parser = argparse.ArgumentParser(
        description="Research and Preparation Agent for job searching and application materials"
    )
    parser.add_argument(
        "--config",
        help="Path to configuration file",
        default=None
    )
    parser.add_argument(
        "--search",
        help="Search for jobs",
        action="store_true"
    )
    parser.add_argument(
        "--analyze",
        help="Analyze saved job listings",
        action="store_true"
    )
    parser.add_argument(
        "--prepare",
        help="Prepare application materials",
        action="store_true"
    )
    
    args = parser.parse_args()
    
    # Initialize configuration
    if args.config:
        config_manager.__init__(args.config)
    
    # Print welcome message
    print("Research and Preparation Agent")
    print("-----------------------------")
    
    if not (args.search or args.analyze or args.prepare):
        print("No action specified. Use --search, --analyze, or --prepare.")
        return
    
    if args.search:
        print("Job search functionality not yet implemented.")
    
    if args.analyze:
        print("Job analysis functionality not yet implemented.")
    
    if args.prepare:
        print("Materials preparation functionality not yet implemented.")


if __name__ == "__main__":
    sys.exit(main())