import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
 
from cli import CLI
 
 
def main() -> None:
    cli = CLI()
    cli.run()
 
main()