import scrapy
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient


class AvitoImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['images']:
            for img in item['images']:
                try:
                    yield scrapy.Request(img)
                except TypeError as e:
                    print(e)
        return item

    def item_completed(self, results, item, info):
        if results:
            item['images'] = [itm[1] for itm in results if itm[0]]
        return item


class MongoPipeline(object):
    def __init__(self):
        MONGO_URI = 'mongodb://172.17.0.2:27017/'
        MONGO_DATABASE = 'avito_db'

        client = MongoClient(MONGO_URI)
        self.mongo_base = client[MONGO_DATABASE]

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item