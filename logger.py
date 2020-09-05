import logging.config

def init():
    logging.config.fileConfig('./conf/logging.conf')

    logger = logging.getLogger('simpleExample')

    logger.info('sss')


if __name__ == '__main__':
    init()
