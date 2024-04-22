![0_4OzHbhhH-jHJHg_t](https://github.com/chloe0524/holbertonschool-web_back_end/assets/127857895/536fa87f-cdc1-47fb-bd16-81f8fb54ed80)

### Python - Async Comprehension

1. :round_pushpin: **Async Generator**
   - Write a coroutine called `async_generator` that loops 10 times, waits asynchronously for 1 second each time, then yields a random number between 0 and 10.

2. :round_pushpin:**Async Comprehensions**
   - Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`, then returns the 10 random numbers.

3. :round_pushpin:**Run time for four parallel comprehensions**
   - Import `async_comprehension` from the previous file and write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.
