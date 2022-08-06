import sys

from ThreadParser import ThreadParser
from ThreadPublisher import ThreadPublisher
from Twitter import Twitter

if __name__ == '__main__':
    twitter = Twitter()
    thread_parser = ThreadParser(sys.argv[1])
    thread_parser()

    publisher = ThreadPublisher(twitter.oauth, thread_parser.thread)
    publisher()


