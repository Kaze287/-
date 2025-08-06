import random
import time
import logging
import traceback

from people_on_weibo import PeopleOnWeibo

if __name__ == '__main__':
    while True:
        try:
            logging.basicConfig(level=logging.DEBUG,
                                filename=f'logs/{int(time.time())}.log',
                                filemode='w',
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
            try:
                people = PeopleOnWeibo()
                people.pause(14, 17)
                logging.debug('Successfully started Weibo.')

                while True:
                    choice = random.randint(1, 3)
                    if choice == 1:
                        people.scroll_up()
                        people.pause(16, 24)
                        logging.debug('Successfully scrolled up.')

                    elif choice == 2:
                        # 随机刷新
                        people.refresh()
                        people.pause(16, 24)
                        logging.debug('Successfully refreshed.')

                    elif choice == 3:
                        # 随机关注到某卡片
                        people.focus_card(1)
                        people.pause(4, 8)
                        logging.debug('Successfully focused card.')

                        people.click_like()
                        people.pause(4, 8)
                        logging.debug('Successfully clicked like.')

                        content = people.read_content()
                        logging.debug('Successfully read content.')
                        print(content)

                        people.save_elemshot(people.focused_card)
                        people.pause(4, 8)
                        logging.debug('Successfully saved element screenshot.')
            except Exception as e:
                logging.error(e)
                traceback.print_exc()
            finally:
                try:
                    people.driver.quit()
                except Exception as e:
                    logging.error(e)
                    traceback.print_exc()
        except Exception as e:
            print(e)
            time.sleep(10)