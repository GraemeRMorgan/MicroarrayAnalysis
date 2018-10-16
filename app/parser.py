from app.database import get_database
import click

# parses a .csv that is passed to it.  Creates an array with
# the data
def parse(file):
    file_contents_by_row = []
    last_line = None
    first_line = True
    with open(file) as sample_file:
        for line in sample_file:
            if first_line:
                first_line = False
            elif not last_line:
                row = line.split('\t')
                file_contents_by_row.append(row)
    print(file_contents_by_row[0])
    fill_database(file_contents_by_row)


# fills the database with an array that is passed with it
def fill_database(file_contents_by_row):

    db = get_database()

    for x in file_contents_by_row[1: ]:
        db.execute('''INSERT INTO mergedGenes(tracking_id, locus, h1tl_fpkm, h3tl_fpkm, h1tr_fpkm, c1tr_fpkm, c2br_fpkm, c3tr_fpkm) VALUES(?,?,
            ?,?,?,?,?,?)''', (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
    db.commit()
    click.echo('database filled')

