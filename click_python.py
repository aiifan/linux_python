import click

@click.command()
@click.option('--count', default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="the person to greet.")
def hello(count, name):
    """simple program that greets NAME fora total of COUNT times."""
    for x in range(count):
        click.echo("hello %s! " %name)
if __name__ =="__main__":
    hello()