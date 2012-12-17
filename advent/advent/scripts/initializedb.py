import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from ..models import Base, DBSession
from ..models import Group, Student


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    ## use: $ alembic upgrade head
    # Base.metadata.create_all(engine)
    with transaction.manager:
        do_initialize()

def do_initialize():
    g = Group(name=u"Gryffindor", short_name=u"red")
    h = Group(name=u"Hufflepuff", short_name=u"yellow")
    r = Group(name=u"Ravenclaw", short_name=u"blue")
    s = Group(name=u"Slytherin", short_name=u"green")

    g.students.append(Student(name=u"aaa", grade=1))
    g.students.append(Student(name=u"bbb", grade=1))
    g.students.append(Student(name=u"ccc", grade=1))

    h.students.append(Student(name=u"hhh", grade=1))
    h.students.append(Student(name=u"iiii", grade=1))

    r.students.append(Student(name=u"rrr", grade=1))
    r.students.append(Student(name=u"ssss", grade=1))
    r.students.append(Student(name=u"tttttt", grade=1))
    r.students.append(Student(name=u"uu", grade=1))

    s.students.append(Student(name=u"xxxx", grade=1))
    s.students.append(Student(name=u"yyy", grade=1))
    s.students.append(Student(name=u"z", grade=1))

    DBSession.add_all([g, h, r, s])

