import yaml
import click
from rich.console import Console
from rich.table import Table

# Import the factory function from the core module we built
from core.auditor import get_auditor

console = Console()

@click.command()
def run_audit():
    """Run the CIS Benchmark audit for the current operating system."""
    
    # 1. Initialize the correct auditor for this OS
    try:
        auditor = get_auditor()
        console.print(f"[bold blue]Starting CIS Audit for {auditor.os_type}...[/bold blue]\n")
    except OSError as e:
        console.print(f"[bold red]{e}[/bold red]")
        return

    # 2. Select the correct YAML file based on the OS
    if auditor.os_type == "Windows":
        rule_file = "rules/windows_rules.yaml"
    else:
        rule_file = "rules/linux_rules.yaml"

    # 3. Load the YAML rules
    try:
        with open(rule_file, "r") as file:
            benchmark_data = yaml.safe_load(file)
            rules = benchmark_data.get("rules", [])
    except FileNotFoundError:
        console.print(f"[bold red]Error: Could not find {rule_file}[/bold red]")
        return

    # 4. Set up the Rich Table for terminal output
    table = Table(title=f"{auditor.os_type} CIS Benchmark Results")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title", style="white")
    table.add_column("Status", justify="center")

    passed_count = 0
    failed_count = 0

    # 5. Loop through the rules and execute them
    for rule in rules:
        is_compliant = auditor.evaluate_rule(rule)
        
        if is_compliant:
            status = "[bold green]PASS[/bold green]"
            passed_count += 1
        else:
            status = "[bold red]FAIL[/bold red]"
            failed_count += 1
            
        table.add_row(rule["id"], rule["title"], status)

    # 6. Print the table and a summary
    console.print(table)
    console.print(f"\n[bold]Audit Complete![/bold] Passed: [green]{passed_count}[/green] | Failed: [red]{failed_count}[/red]")

if __name__ == '__main__':
    run_audit()
