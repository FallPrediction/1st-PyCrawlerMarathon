import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# get_project_settings() 方法會取得爬蟲專案中的 settings.py 檔案設定，啟動爬蟲前要提供這些設定給 Scrapy Engine


def main():
    #target_board = ['Gossiping', 'Stock']
    target_board = ['Gossiping']
    process = CrawlerProcess(get_project_settings())
    for board in target_board:
        process.crawl('PTTCrawler', board=board)
        process.start()

if __name__ == '__main__':
    main()
