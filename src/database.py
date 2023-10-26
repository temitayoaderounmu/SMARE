from dotenv import load_dotenv
import pymongo
import os

def get_conn(db):
  # load environment variable containing db uri (which includes username and password)
  load_dotenv()
  db_uri = os.getenv("DB_URI")

  # create a mongodb connection
  try:
    client = pymongo.MongoClient(db_uri)
    
  # return a friendly error if a URI error is thrown 
  except pymongo.errors.ConfigurationError:
    print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string (found the .env)?")
    return {"success" : False, "db": 0}

  # use a database named "Test"
  return {"success" : True, "db": client.get_database(db)}

def post_one(db, collection, title, price, location, miles, link):
  car = {
    "title": title, 
    "price": price, 
    "location": location, 
    "miles": miles, 
    "link": link
  }
  
  # insert into collection called "scrape_test"
  conn = get_conn(db)

  if (conn["success"]):
    result = conn["db"][collection].insert_one(car)
    return result.acknowledged
  else:
    return False