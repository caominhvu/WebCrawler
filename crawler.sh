#!/bin/bash

scrapy crawl vnexpress --set FEED_URI=thoisu.json --set FEED_FORMAT=json -a category="thoisu/1001005" -a total_article=1500

scrapy crawl vnexpress --set FEED_URI=otoxemay.json --set FEED_FORMAT=json -a category="oto-xemay/1001006" -a total_article=1500

scrapy crawl vnexpress --set FEED_URI=thegioi.json --set FEED_FORMAT=json -a category="thegioi/1001002" -a total_article=1500

scrapy crawl vnexpress --set FEED_URI=phapluat.json --set FEED_FORMAT=json -a category="phapluat/1001007" -a total_article=1500

scrapy crawl vnexpress --set FEED_URI=sohoa_sanpham.json --set FEED_FORMAT=json -a category="sohoa/san-pham/1002593" -a total_article=1500

mv *.json ../NaiveBayes/data