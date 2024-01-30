from threading import Thread
import time

timeout_seconds = 3

def fn(i: int) -> int:
    print(f'executing...: {i}')
    time.sleep(10)
    print(f'finished...: {i}')
    return i + 1

def run() -> None:
    ls = [1, 2, 3]
    threads = []
    
    for l in ls:
        thread = Thread(target=fn, args=(l, ))
        thread.start()
        threads.append(thread)
    
    print('before joining threads...')
    for t in threads:
        t.join(timeout=timeout_seconds)

        if t.is_alive():
            print('thread timed out ..')
        else:
            print('thread has terminated')


if __name__ == '__main__':
    run()