#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Kubernetes CLI
Author: Daniel West
Version: 0.2
"""

import subprocess
import sys
import shlex

import click

APP_HELP = (
    "\nKUBERNETES CLI\n"
    "Run: python .\\kub_shell.py <command>    to run kubectl commands\n"
    "Or : python .\\kub_shell.py --shell, -s       for shell mode\n"
)

@click.group(invoke_without_command=True, help=APP_HELP)
@click.option("--shell","-s", is_flag=True, help="Start an interactive shell.")
@click.pass_context
def cli(ctx, shell):
    if ctx.invoked_subcommand is None and (shell or len(sys.argv) == 1):
        shell_loop()
        ctx.exit(0)


# -----------------------------
# kubectl commands with help
# -----------------------------

@cli.command(help="- List configured kubectl clusters")
def clusters():
    run_kubectl(["config", "get-clusters"])


# switch to dev cluster
@cli.command(help="- Switch to Development cluster")
def dev_cluster():
    run_kubectl(["config", "use-context", "development"])

# switch to platform cluster
@cli.command(help="- Switch to Platform cluster")
def plf_cluster():
    run_kubectl(["config", "use-context", "platform"])


# current cluster
@cli.command(name="?", help="- Current cluster")
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
def what_cluster(args):
    click.echo("You are in: ", nl=False)
    run_kubectl(["config", "current-context"])


# cpu
@cli.command(help="- List cpu usage")
def cpu():
    run_kubectl(["top", "nodes"])

# list nodes
@cli.command(help="- List nodes")
def nodes():
    run_kubectl(["get", "nodes"])

# list nodes with all information
@cli.command(help="- List nodes - more information")
def nodes_more():
    run_kubectl(["get", "nodes", "-o", "wide"])

# list pods
@cli.command(help="- List pods (current namespace)")
def pods():
    run_kubectl(["get", "pods"])

# list namespaces
@cli.command(help="- List deployments across all namespaces")
def dep():
    run_kubectl(["get", "deployments", "-A"])


# -----------------------------
# Core runner
# -----------------------------

def run_kubectl(args) -> int:
    cmd = ["kubectl"] + list(args)
    try:
        result = subprocess.run(cmd, text=True, capture_output=True)
        if result.stdout:
            click.echo(result.stdout, nl=False)
        # print stderr on failure (adjust if you want stderr always)
        if result.stderr and result.returncode != 0:
            click.echo(result.stderr, err=True, nl=False)
        return result.returncode
    except FileNotFoundError:
        click.echo("Error: 'kubectl' not found on PATH.", err=True)
        return 127


# -----------------------------
# Shell loop
# -----------------------------

def shell_loop():
    # Optional: enable history on Unix; ignore on Windows
    try:
        import readline  # noqa: F401
    except Exception:
        pass

    click.echo("|--------------------------------- KUBE Shell --------------------------------------------|")
    click.echo("|-----------------------------------------------------------------------------------------|")
    click.echo("|Options: nodes | nodes-more | pods | dep | cpu | ? | dev-cluster | plf-cluster | clusters|")
    click.echo("|-----------------------------------------------------------------------------------------|")
    click.echo("'kubectl <command>' also accepted input")
    click.echo("Type 'exit' or 'quit' to leave. --help for help\n")

    while True:
        try:
            line = input("K> ").strip()
        except EOFError:
            click.echo("\nEOF. Bye!")
            break
        except KeyboardInterrupt:
            click.echo("\nInterrupted. Bye!")
            break

        if not line:
            continue
        lower = line.lower()
        if lower in {"exit", "quit", "q"}:
            click.echo("Bye!")
            break
        if lower in {"66", "order 66"}:
            click.echo("Yes my lord")
            break
        # If user typed a raw kubectl command, run it directly
        if lower.startswith("kubectl "):
            rest = line.split(" ", 1)[1]
            args = shlex.split(rest)
            _ = run_kubectl(args)
            continue
        if lower in {"jose"}:
            click.echo("Did you mean Joes?")
            continue
        # Otherwise, treat it as our Click command line
        try:
            args = shlex.split(line)
            # Invoke Click programmatically without exiting the whole process
            cli.main(args=args, standalone_mode=False)
        except SystemExit as e:
            # Swallow Click's SystemExit to keep the REPL alive
            if e.code not in (0, None):
                click.echo(f"(command exited with code {e.code})", err=True)
        except Exception as exc:
            click.echo(f"Error: {exc}", err=True)
if __name__ == "__main__":
    cli()
