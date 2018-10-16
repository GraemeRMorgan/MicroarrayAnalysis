import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_database():
    if'database' not in g:
        g.database = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.database.row_factory = sqlite3.Row

    return g.database

def close_database(e=None):
    database = g.pop('database', None)
    if database is not None:
        database.close()

def init_database():
    database = get_database()
    with current_app.open_resource('schema.sql') as f:
        database.executescript(f.read().decode('utf8'))

def fetch_database(field):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''SELECT ''' + field + ''' FROM mergedGenes''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row[0])

@click.command('init_database')
@with_appcontext
def init_database_command():
    init_database()
    click.echo('Initialized the database')

@click.command('fetch_database')
@click.argument('field')
@with_appcontext
def fetch_database_command(field):
    fetch_database(field)

@click.command('fill_database')
@click.argument('file')
@with_appcontext
def fill_database_command(file):
    from . import parser
    parser.parse(file)

def init_app(app):
    app.teardown_appcontext(close_database)
    app.cli.add_command(init_database_command)
    app.cli.add_command(fill_database_command)
    app.cli.add_command(fetch_database_command)