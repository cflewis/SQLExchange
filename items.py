from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime

Base = declarative_base()

datetimeFormat = '%Y-%m-%dT%H:%M:%S.%f'

class Badge(Base):
    __tablename__ = 'Badges'
    __table_args__ = {'mysql_engine':'InnoDB'}

    Id = Column(Integer, primary_key=True)
    UserId = Column(Integer)
    Name = Column(String(50))
    Date = Column(DateTime)

    def __init__(self, id, userId, name, date):
        self.Id = id
        self.UserId = userId
        self.Name = name
        self.Date = date

    def __repr__(self):
        stringData = (self.Id, self.UserId, self.Name, self.Date)
        return "<Badge Id: %d, UserId: %d, Name: %s, Date: %s>" % stringData

    @staticmethod
    def parseRow(element):
        return Badge(int(element.attrib['Id']),
                     int(element.attrib['UserId']),
                     element.attrib['Name'],
                     datetime.strptime(element.attrib['Date'], datetimeFormat))

class Comment(Base):
    __tablename__ = 'Comments'
    __table_args__ = {'mysql_engine':'InnoDB'}

    Id = Column(Integer, primary_key=True)
    PostId = Column(Integer)
    Score = Column(Integer)
    Text = Column(Text(600))
    CreationDate = Column(DateTime)
    UserDisplayName = Column(String(30))
    UserId = Column(Integer)

    def __init__(self):
        pass

    def __repr__(self):
        stringData = (self.Id, self.PostId, self.Score, self.CreationDate)
        return "<Comment Id: %s, PostId: %s, Score: %s, CreationDate: %s>" % stringData

    @staticmethod
    def parseRow(element):
        comment = Comment()

        for key, value in element.attrib.items():
            if key == 'Id':
                comment.Id = value
            elif key == 'PostId':
                comment.PostId = value
            elif key == 'Score':
                comment.Score = value
            elif key == 'Text':
                comment.Text = value
            elif key == 'CreationDate':
                comment.CreationDate = datetime.strptime(value, datetimeFormat)
            elif key == 'UserDisplayName':
                comment.UserDisplayName = value
            elif key == 'UserId':
                comment.UserId = int(value)

        return comment

class Post(Base):
    __tablename__ = 'Posts'
    __table_args__ = {'mysql_engine':'InnoDB'}

    Id = Column(Integer, primary_key=True)
    PostTypeId = Column(Integer)
    AcceptedAnswerId = Column(Integer)
    ParentId = Column(Integer)
    CreationDate = Column(DateTime)
    Score = Column(Integer)
    ViewCount = Column(Integer)
    Body = Column(Text)
    OwnerUserId = Column(Integer)
    LastEditorUserId = Column(Integer)
    LastEditorDisplayName = Column(String(40))
    LastEditDate = Column(DateTime)
    LastActivityDate = Column(DateTime)
    CommunityOwnedDate = Column(DateTime)
    ClosedDate = Column(DateTime)
    Title = Column(String(250))
    Tags = Column(String(150))
    AnswerCount = Column(Integer)
    CommentCount = Column(Integer)
    FavoriteCount = Column(Integer)

    def __init__(self):
        pass

    def __repr__(self):
        return "<Post>"

    @staticmethod
    def parseRow(element):
        post = Post()

        for key, value in element.attrib.items():
            if key == 'Id':
                post.id = int(value)
            elif key == 'PostTypeId':
                post.PostTypeId = int(value)
            elif key == 'ParentId':
                post.ParentId = int(value)
            elif key == 'AcceptedAnswerId':
                post.AcceptedAnswerId = int(value)
            elif key == 'CreationDate':
                post.CreationDate = datetime.strptime(value, datetimeFormat)
            elif key == 'Score':
                post.Score = int(value)
            elif key == 'ViewCount':
                try:
                    post.ViewCount = int(value)
                except ValueError:
                    # Some ViewCounts aren't filled in
                    pass
            elif key == 'Body':
                post.Body = value
            elif key == 'OwnerUserId':
                post.OwnerUserId = int(value)
            elif key == 'LastEditorUserId':
                post.LastEditorUserId = int(value)
            elif key == 'LastEditorDisplayName':
                post.LastEditorDisplayName = value
            elif key == 'LastEditDate':
                post.LastEditDate = datetime.strptime(value, datetimeFormat)
            elif key == 'LastActivityDate':
                post.LastActivityDate = datetime.strptime(value, datetimeFormat)
            elif key == 'CommunityOwnedDate':
                post.CommunityOwnedDate = datetime.strptime(value, datetimeFormat)
            elif key == 'ClosedDate':
                post.ClosedDate = datetime.strptime(value, datetimeFormat)
            elif key == 'Title':
                post.Title = value
            elif key == 'Tags':
                post.Tags == value
            elif key == 'AnswerCount':
                post.AnswerCount = int(value)
            elif key == 'CommentCount':
                post.CommentCount = int(value)
            elif key == 'FavoriteCount':
                post.FavoriteCount = int(value)

        return post

class User(Base):
    __tablename__ = 'Users'
    __table_args__ = {'mysql_engine':'InnoDB'}

    Id = Column(Integer, primary_key=True)
    Reputation = Column(Integer)
    CreationDate = Column(DateTime)
    DisplayName = Column(String(40))
    EmailHash = Column(String(32))
    LastAccessDate = Column(DateTime)
    WebsiteUrl = Column(String(200))
    Location = Column(String(100))
    Age = Column(Integer)
    AboutMe = Column(Text)
    Views = Column(Integer)
    UpVotes = Column(Integer)
    DownVotes = Column(Integer)

    def __init__(self):
        pass

    def __repr__(self):
        return "<User>"

    @staticmethod
    def parseRow(element):
        user = User()

        for key, value in element.attrib.items():
            if key == 'Id':
                user.id = int(value)
            elif key == 'Reputation':
                user.Reputation = int(value)
            elif key == 'CreationDate':
                user.CreationDate = datetime.strptime(value, datetimeFormat)
            elif key == 'DisplayName':
                user.DisplayName = value
            elif key == 'EmailHash':
                user.EmailHash = value
            elif key == 'LastAccessDate':
                user.LastAccessDate = value
            elif key == 'WebsiteUrl':
                user.WebsiteUrl = value
            elif key == 'Location':
                user.Location = value
            elif key == 'Age':
                user.age = int(value)
            elif key == 'AboutMe':
                user.AboutMe = value
            elif key == 'Views':
                user.Views = int(value)
            elif key == 'UpVotes':
                user.UpVotes = int(value)
            elif key == 'DownVotes':
                user.DownVotes = int(value)

        return user
