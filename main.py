# coding: utf-8

__author__ = 'xiayf'

import multiprocessing

from parsers import *

CONFIGS = [
    {
        'name': u'网贷之家 - 问答',
        'url': 'http://www.wangdaizhijia.com/wenda/c-all/all/',
        'parser': WangDaiZhiJiaParser,
    },
    {
        'name': u'网贷天眼 - 已解决问题',
        'url': 'http://www.p2peye.com/ask/a2/',
        'parser': WangDaiTianYanParser,
    },
    {
        'name': u'网贷天眼 - 待解决问题',
        'url': 'http://www.p2peye.com/ask/a1/',
        'parser': WangDaiTianYanParser,
    },
    {
        'name': u'积木盒子 - 理财心得 - 投资心得',
        'url': 'http://bbs.jimubox.com/thread-12?type=22&orderby=postdate',
        'parser': JiMuBoxParser,
    },
    {
        'name': u'积木盒子 - 理财心得 - 金融观察',
        'url': 'http://bbs.jimubox.com/thread-12?type=24&orderby=postdate',
        'parser': JiMuBoxParser,
    },
    {
        'name': u'积木盒子 - 理财心得 - 理财指南',
        'url': 'http://bbs.jimubox.com/thread-12?type=27&orderby=postdate',
        'parser': JiMuBoxParser,
    }
]


class Crawler(object):

    @classmethod
    def run(cls):
        process_records = []
        for config in CONFIGS:
            parser_class = config.pop('parser')
            target_parser = parser_class(config)
            new_process = multiprocessing.Process(target=target_parser.run)
            new_process.start()
            process_records.append(new_process)

        for pr in process_records:
            pr.join()


if __name__ == '__main__':
    Crawler.run()