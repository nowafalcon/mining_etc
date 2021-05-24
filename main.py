import os
import dotenv
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
#from Insta.spiders.autoyoula import AutoyoulaSpider
from Insta.spiders.instagram import InstagramSpider


if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    crawler_settings = Settings()
    crawler_settings.setmodule("Insta.settings")
    crawler_process = CrawlerProcess(settings=crawler_settings)
    tags = ["python"]
    crawler_process.crawl(
        InstagramSpider,
        login=os.getenv("INST_LOGIN"),
        password=os.getenv("INST_PASSWD"),
        tags=tags,
    )
    crawler_process.start()