from rich.console import Console
import os
import delcaches_folder
def Main():
    console = Console()
    console.print("[bold rgb(120,0,0)]Clearing Game Cache for The Sims 3...[/bold rgb(120,0,0)]")
    delcaches_folder.DeletesXML()
    delcaches_folder.DeletesCache()
    console.print("[bold rgb(0,155,0)]Success!!!\nCreated by Ittokichiko(Created Organization by Rikko Matsumato)[/bold rgb(0,155,0)]")
    os._exit(4456)
    

if __name__ == "__main__":
    Main()