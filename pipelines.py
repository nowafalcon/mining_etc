from itemadapter import ItemAdapter
from .settings import BOT_NAME
from pymongo import MongoClient


class GbParsePipeline:
    def process_item(self, item, spider):
        return item


class GbMongoPipeline:
    def __init__(self):
        client = MongoClient()
        self.db = client[BOT_NAME]

    def process_item(self, item, spider):
        self.db[spider.name].insert_one(item)
        return item