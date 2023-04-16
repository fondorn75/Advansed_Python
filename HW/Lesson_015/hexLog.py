import logging


def log_all():
    logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
    logger.info('Немного информации о работе кода')
    logger.warning('Внимание! Надвигается буря!')
    logger.error('Поймали ошибку. Дальше только неизвестность')
    logger.critical('На этом всё')


if __name__ == '__main__':
    logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger('Основной файл проекта')
    logger.warning('Внимание! Используем вызов функции из другого модуля')
    log_all()