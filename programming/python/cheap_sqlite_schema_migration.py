#!/usr/bin/env python3

"""
Example of how to perform cheap database schema migrations when an app starts.
Very cheap, it only handles upgrades, not downgrades.
Not really handles errors, make sure your migrations are robust!
"""

import sqlite3

# Schema updates

# key: version to reach from preceding version
# value: list of statements to execute

UPGRADES = {
    0: [  # v0
        'INSERT INTO version VALUES(0)',  # always keep for v0
        # put base schema here
        '''
        CREATE TABLE IF NOT EXISTS notebook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note TEXT
        )
        ''',
    ],
    1: [  # v1
        'ALTER TABLE notebook ADD COLUMN updated_at TEXT',
    ],
    # add new versions here
}


def migrate_to_latest_version(db):
    """Perform database schema updates incrementally"""

    c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS version (version INTEGER PRIMARY KEY)')

    base_version = 0
    for row in db.execute('SELECT version FROM version'):
        base_version = row[0]

    for ver in range(base_version, max(UPGRADES) + 1):
        with db:
            for stmt in UPGRADES[ver]:
                try:
                    db.execute(stmt)
                except sqlite3.Error as exc:
                    print('Failed to run migration to version %s instruction %r: %s' % (ver, stmt, exc))
                    raise

            try:
                db.execute('UPDATE version SET version = ?', (ver + 1,))
            except sqlite3.Error as exc:
                print('Failed to run update to version %s: %s' % (ver + 1, stmt, exc))
                raise


# open db and update to latest schema version
db = sqlite3.connect('./file.sqlite')
migrate_to_latest_version(db)
