# 1
import time
import threading

def make_tea(name, seconds):
    print(f"{name} იწყება")
    time.sleep(seconds)
    print(f"{name}: მზადაა")

teas = {
    "მწვანე ჩაი": 1.0,
    "შავი ჩაი": 1.5,
    "ბალახის ჩაი": 2.0
}
start = time.perf_counter()
for tea, sec in teas.items():
    make_tea(tea, sec)
end = time.perf_counter()
first = round(end - start, 2)
print("თანმიმდევრულად:", round(end - start, 2))

thread = []

start = time.perf_counter()

for tea, sec in teas.items():
    t = threading.Thread(target=make_tea, args=(tea, sec))
    t.start()
    thread.append(t)

for t in thread:
    t.join()
end = time.perf_counter()
second = round(end - start, 2)
print("thread-ებით:", round(end - start, 2), "წმ")
print(f"დაჩქარება: {(first / second):.1f}x")

# 2

import multiprocessing
import time
import threading


def cpu_task(n):
    while n > 0:
        n -= 1


def io_task(seconds):
    time.sleep(seconds)


def run_sequential(task, jobs):
    for job in jobs:
        task(job)


def run_threads(task, jobs):
    threads = []

    for job in jobs:
        t = threading.Thread(target=task, args=(job,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def run_processes(task, jobs):
    processes = []

    for job in jobs:
        p = multiprocessing.Process(target=task, args=(job,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


def measure(runner, task, jobs):
    start = time.perf_counter()
    runner(task, jobs)
    end = time.perf_counter()
    return end - start


cpu_jobs = [10_000_000] * 4
io_jobs = [1.0] * 4


if __name__ == "__main__":

    cpu_seq = measure(run_sequential, cpu_task, cpu_jobs)
    cpu_threads = measure(run_threads, cpu_task, cpu_jobs)
    cpu_processes = measure(run_processes, cpu_task, cpu_jobs)

    io_seq = measure(run_sequential, io_task, io_jobs)
    io_threads = measure(run_threads, io_task, io_jobs)
    io_processes = measure(run_processes, io_task, io_jobs)


    print("\n             თანმიმდევრულად   |    thread-ები     |     პროცესები")

    print(
        f"CPU-bound    {cpu_seq:.2f} წმ ({1.0:.1f}x)    |    " 
        f"{cpu_threads:.2f} წმ ({cpu_seq / cpu_threads:.1f}x)   |   "
        f"{cpu_processes:.2f} წმ ({cpu_seq / cpu_processes:.1f}x)"
    )

    print(
        f"I/O-bound    {io_seq:.2f} წმ ({1.0:.1f}x)    |   "
        f"{io_threads:.2f} წმ ({io_seq / io_threads:.1f}x)   |    "
        f"{io_processes:.2f} წმ ({io_seq / io_processes:.1f}x)"
    )
