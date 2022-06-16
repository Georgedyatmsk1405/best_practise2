import logging
import threading
import random
import time

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

class Context(threading.Thread):
    def __init__(self,name,left_fork,right_fork):
        threading.Thread.__init__(self)
        self.left_fork=left_fork
        self.right_fork=right_fork
        self.name=name

    def __enter__(self):
        self.left_fork.acquire()
        logger.info(f'Philosopher {self.name} acquired left fork')
        
    def __exit__(self,name,left_fork,right_fork):
        if self.right_fork.locked():
                    pass

        self.right_fork.acquire()
        logger.info(f'Philosopher {self.name} acquired right fork')
        logger.info(f'Philosopher {self.name} starts eating.')
        time.sleep(random.randint(1, 10))
        logger.info(f'Philosopher {self.name} finishes eating and leaves to think.')
        self.right_fork.release()
        self.left_fork.release()




class Philosopher(threading.Thread):
    running = True  # used to check if everyone is finished eating

    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            logger.info(f'Philosopher {self.getName()} start thinking.')
            # Philosopher is thinking (but really is sleeping).
            time.sleep(random.randint(1, 10))
            logger.info(f'Philosopher {self.getName()} is hungry.')
            with Context(self.getName(),self.left_fork,self.right_fork):
                print('ok')

  
        


def main():
    forks = [threading.Lock() for n in range(5)]  # initialising array of Lock's i.e forks

    # here (i+1)%5 is used to get right and left forks circularly between 1-5
    philosophers = [
        Philosopher(forks[i % 5], forks[(i + 1) % 5])
        for i in range(5)
    ]
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(200)
    Philosopher.running = False
    logger.info("Now we're finishing.")


if __name__ == "__main__":
    main()
