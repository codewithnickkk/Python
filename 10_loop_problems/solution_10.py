#Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.
import time

wait_time = 1
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    print("attempts",attempts + 1,"wait time",wait_time)
    wait_time *= 2
    attempts += 1
    time.sleep(wait_time)