### Python - Async Comprehension

1. **Async Generator**
   - Write a coroutine called `async_generator` that loops 10 times, waits asynchronously for 1 second each time, then yields a random number between 0 and 10.

2. **Async Comprehensions**
   - Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`, then returns the 10 random numbers.

3. **Run time for four parallel comprehensions**
   - Import `async_comprehension` from the previous file and write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.
