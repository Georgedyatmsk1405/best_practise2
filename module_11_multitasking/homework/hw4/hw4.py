import logging
import random
import threading
import time
Total_sold=0
TOTAL_TICKETS = 10
posad_mesta=40
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore,n):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        self.n=n
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        global posad_mesta
        global Total_sold
        is_running = True
        while Total_sold<=posad_mesta:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                if TOTAL_TICKETS==self.n:
                    TOTAL_TICKETS += posad_mesta-Total_sold

                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                Total_sold+=1
                logger.info(f'{self.getName()} sold one;  {TOTAL_TICKETS} left')
        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


def main():
    semaphore = threading.Semaphore()
    sellers = []
    n=4
    for _ in range(n):
        seller = Seller(semaphore,n)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()
