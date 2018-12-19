from scheduler.main import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    s = Scheduler()
    s.run()


if __name__ == '__main__':
    main()