from mongoengine import Document, StringField, EmailField, IntField
from mongoengine import signals


class Counter(Document):
    name = StringField(required=True, unique=True)
    count = IntField(default=0)

    @classmethod
    def get_next_value(cls, name):
        counter = cls.objects(name=name).modify(upsert=True, new=True, inc__count=1)
        return counter.count


class User(Document):
    id = IntField(primary_key=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    phone = StringField(max_length=10)

    def to_json(self):
        json_data = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone
        }
        return json_data


@signals.pre_save.connect
def assign_auto_increment_id(sender, document, **kwargs):
    if isinstance(document, User) and document.id is None:
        document.id = Counter.get_next_value("id")