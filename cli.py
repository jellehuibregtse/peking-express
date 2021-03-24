import ast
import json
from timeit import default_timer as timer

import click
from pyfiglet import Figlet

import peking_express


def solve_peking(path: str) -> list:
    start = timer()
    file = read_file(path)
    peking = peking_express.PekingExpress(json.loads(file[0]), int(file[1]), int(file[2]), ast.literal_eval(file[3]))
    peking.solve()
    return [peking, (timer() - start)]


def read_file(path: str) -> list:
    with open(path, 'r', encoding='utf8') as file:
        return file.read().split('\n')


@click.group()
def main():
    """
    Simple CLI for getting the path for Peking Express.
    """
    pass


@main.command()
@click.argument('path')
@click.option('--io/--no-io', default=False)
def solve(path: str, io):
    """
    This returns the optimal path in Peking Express given a file.
    """
    f = Figlet(font='big')
    result = solve_peking(path)

    if io:
        click.echo(f.renderText('PEKING'))
        click.echo('INPUT')
        click.echo(f'Graph:\n{result[0].pekingMap.print_graph()}')
        click.echo(f'Critical vertices: {[i.index for i in result[0].pekingMap.get_critical_vertices()]}')
        click.echo(f'Starting vertex: {result[0].startLocation}')

        click.echo('\nOUTPUT')
    click.echo(f'It took {result[1]} seconds to find path: {result[0].get_path()}, using file: \n{path}')


if __name__ == "__main__":
    main()
