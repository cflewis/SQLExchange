from lxml import etree
import items
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def parseXml(xmlFile, rowObject, session):
    for event, element in etree.iterparse(xmlFile):
        if element.tag == 'row':
            row = rowObject.parseRow(element)
            session.add(row)
            session.commit()
            # free this from memory
            element.clear()

def getFileObject(xmlFile):
    # get an iterable
    context = etree.iterparse(xmlFile, events=("start", "end"))

    # turn it into an iterator
    context = iter(context)

    # get the root element
    event, root = context.next()

    if root.tag == 'badges':
        return items.Badge
    elif root.tag == 'comments':
        return items.Comment
    elif root.tag == 'posts':
        return items.Post
    elif root.tag == 'users':
        return items.User

    raise IOError('Unknown XML file')

if __name__ == '__main__':
    files = sys.argv[2:]

    engine = create_engine(sys.argv[1], echo=True)
    items.Base.metadata.create_all(engine)

    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()

    for f in files:
        xmlFile = open(f, 'rb')
        fileObject = getFileObject(xmlFile)
        xmlFile.seek(0)
        parseXml(xmlFile, fileObject, session)

    session.close()