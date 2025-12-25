from rich.console import Console
from rich.markdown import Markdown

console = Console()

markdown = Markdown("# Hello, World!")
console.print(markdown)

console.print("[bold red]Hello[/bold red] [bold green]World[/bold green]!")