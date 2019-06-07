from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, MenuItem, User

engine = create_engine('sqlite:///categorymenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

category1 = Category(user_id=1, name="Sci-Fi")

session.add(category1)
session.commit()

category2 = Category(user_id=1, name="Action")

session.add(category2)
session.commit()


category3 = Category(user_id=1, name="Romance")

session.add(category3)
session.commit()


menuItem2 = MenuItem(user_id=1, name="Avengers", description="Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
                     category=category1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(user_id=1, name="Die Hard", description="An NYPD officer tries to save his wife and several others taken hostage by German terrorists during a Christmas party at the Nakatomi Plaza in Los Angeles.",
                     category=category2)

session.add(menuItem3)
session.commit()


menuItem5 = MenuItem(user_id=1, name="Sweet November", description="A workaholic executive, and an unconventional woman agree to a personal relationship for a short period. In this short period she changes his life.",
                     category=category3)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Avengers End Game", description="Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe.",
                     category=category1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="The Fault in Our Stars", description="Hazel Grace Lancaster (Shailene Woodley), a 16-year-old cancer patient, meets and falls in love with Gus Waters (Ansel Elgort), a similarly afflicted teen from her cancer support group. Hazel feels that Gus really understands her. They both share the same acerbic wit and a love of books, especially Grace's touchstone, 'An Imperial Affliction' by Peter Van Houten. When Gus scores an invitation to meet the reclusive author, he and Hazel embark on the adventure of their brief lives.",
                     category=category3)

session.add(menuItem7)
session.commit()

print "added menu items!"
