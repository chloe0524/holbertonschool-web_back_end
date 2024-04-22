![1_dZBikGD1DDmrqTbhI_qvUw](https://github.com/chloe0524/holbertonschool-web_back_end/assets/127857895/76189116-6ef5-4ea7-8600-4bcae1bef2bc)

### Python - Async

1. :round_pushpin:**The basics of async**
   - Write an asynchronous coroutine `wait_random` that waits for a random delay between 0 and `max_delay` seconds and eventually returns it.

2. :round_pushpin:**Let's execute multiple coroutines at the same time with async**
   - Write an async routine `wait_n` that spawns `wait_random` `n` times with the specified `max_delay` and returns the list of all the delays (float values).

3. :round_pushpin:**Measure the runtime**
   - Create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`.

4. :round_pushpin:**Tasks**
   - Write a function `task_wait_random` that takes an integer `max_delay` and returns a asyncio.Task.
   - Alter `wait_n` into a new function `task_wait_n` where `task_wait_random` is being called.
