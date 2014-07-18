# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import csv

class WebcrawlerPipeline(object):
    
#     def process_item(self, item, spider):
#         return item
    def __init__(self):
        self.myCSV = csv.writer(open('output.csv', 'wb'))
        self.myCSV.writerow(['name', 'address','category'])

    def process_item(self, item, spider):
     self.myCSV.writerow([item['name'].encode('utf-8'),
                                    item['address'].encode('utf-8'),
                                    item['category'].encode('utf-8')])

     return item
