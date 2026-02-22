from mongoengine import Document, fields, connect
import mongomock
import unittest


class MyDocument(Document):
    parent = fields.ReferenceField("MyDocument")


class SimpleDocumentTest(unittest.TestCase):

    def test_document(self):
        MyDocument()


class MoreComplexRecursiveDocument(unittest.TestCase):

    def test_import(self):
        connect(
            db="test",
            host="mongodb://dummy_host",
            mongo_client_class=mongomock.MongoClient,
            UuidRepresentation="standard",
        )
        from .fixtures.recursive_definition import UserForm
        UserForm()
