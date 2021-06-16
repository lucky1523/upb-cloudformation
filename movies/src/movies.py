
import json
import boto3
import os

users_table = os.environ['USERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)


def getMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': movie_id,
            'sk': 'age'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    movie_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(movie_id)
    item = {
        'pk': movie_id,
        'sk': 'info',
        'title': body["title"],
        'actors': body["actors"],
        'year': body["year"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def getMovieByRoom(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    movie_id = path.split("/")[-3]
    body = json.loads(event["body"])
    response = table.get_item(
        
        Key = {
            'pk' : room_id,
            'sk' : movie_id
        }    
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
        
    }

# def putMovieByRoom(event, context):
#     print(json.dumps({"running": True}))
#     print(json.dumps(event))
#     path = event["path"]
#     room_id = path.split("/")[-1]
#     movie_id = path.split("/")[-3] # ["user", "id"]
    
#     body = json.loads(event["body"])
#     print(body)
#     print(room_id)
#     print(movie_id)
#     item = {
#         'pk': movie_id+room_id,
#         'sk': '',
#         'atendee': body["atendee"]
      
#     }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def getMoviesWatchedByPerson(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    person_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': person_id,
            'sk': 'movie_id'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putMoviesWatchedByPerson(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    person_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(person_id)
    item = {
        'pk': person_id,
        'sk': 'movie_id',
        'time': body["time"],
        'date': body["date"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
    
def getCinemaRoomInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    response = table.get_item(
        Key={
            'pk': room_id,
            'sk': 'seats'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putCinemaRoomInfo(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    room_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(room_id)
    item = {
        'pk': room_id,
        'sk': 'seats',
        'numberOfSeats': body["numberOfSeats"],
        '3D': body["3D"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }