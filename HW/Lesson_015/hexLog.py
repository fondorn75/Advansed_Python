import logging
import hexametric


if __name__ == '__main__':
    logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.INFO)
    try:
        temp = hexametric.hexCreation('12356')
        logging.info(f" successful with result: {temp}.")
    except Exception as err:
        logging.error(err, exc_info=True)
