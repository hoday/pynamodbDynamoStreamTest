#
# example of a lambda handler triggered off of a dynamo stream
#
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute
)


class Person(Model):
    class Meta:
        table_name = 'Person'

    id = UnicodeAttribute(hash_key=True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()


def lambda_handler(event, context):

    records = event.get("Records")
    for record in records:

        event_name = record.get("eventName")
        dynamodb = record.get("dynamodb")


        if event_name in ("INSERT", "MODIFY"):
            person = Person.from_raw_data (dynamodb.get("NewImage"))
            print(person)
