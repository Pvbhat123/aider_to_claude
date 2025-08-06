import typer
from pathlib import Path
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from .word_counter import word_counter
from .llm import analyze_transcript

app = typer.Typer()
console = Console()


@app.command()
def analyze_transcript(
    path_to_script_text_file: Path = typer.Argument(..., help="Path to the transcript text file"),
    min_count_threshold: int = typer.Option(10, help="Minimum word count threshold")
):
    """
    Analyze a transcript file for word frequency and AI insights.
    
    Usage example:
        uv run python -m spec_based_ai_coding.main analyze-transcript transcript.txt
        uv run python -m spec_based_ai_coding.main analyze-transcript transcript.txt --min-count-threshold 5
    """
    # Read the transcript file
    try:
        with open(path_to_script_text_file, 'r', encoding='utf-8') as f:
            transcript_text = f.read()
    except FileNotFoundError:
        rprint(f"[red]Error: File '{path_to_script_text_file}' not found.[/red]")
        raise typer.Exit(1)
    except Exception as e:
        rprint(f"[red]Error reading file: {e}[/red]")
        raise typer.Exit(1)
    
    # Count words
    console.print("\n[bold cyan]Analyzing transcript...[/bold cyan]\n")
    word_counts = word_counter(transcript_text, min_count_threshold)
    
    # Create a table for word frequencies
    table = Table(title="Word Frequency Analysis")
    table.add_column("Word", style="cyan", no_wrap=True)
    table.add_column("Count", style="magenta", justify="right")
    
    # Add word counts to table
    for word, count in word_counts.count_to_word_map.items():
        table.add_row(word, str(count))
    
    # Print the word frequency table
    console.print(table)
    
    # Perform AI analysis
    try:
        console.print("\n[bold cyan]Getting AI insights...[/bold cyan]\n")
        analysis = analyze_transcript(transcript_text, word_counts.count_to_word_map)
        
        # Print AI analysis results
        console.print("[bold green]Quick Summary:[/bold green]")
        console.print(analysis.quick_summary)
        
        console.print("\n[bold green]Key Highlights:[/bold green]")
        for highlight in analysis.bullet_point_highlights:
            console.print(f"• {highlight}")
        
        console.print(f"\n[bold green]Sentiment:[/bold green] {analysis.sentiment_analysis}")
        
        console.print("\n[bold green]Keywords:[/bold green]")
        console.print(", ".join(analysis.keywords))
        
    except Exception as e:
        rprint(f"\n[yellow]Warning: AI analysis failed: {e}[/yellow]")
        rprint("[yellow]Make sure GEMINI_API_KEY is set in your environment.[/yellow]")


def main():
    """Main entry point for the CLI application."""
    app()


if __name__ == "__main__":
    main()