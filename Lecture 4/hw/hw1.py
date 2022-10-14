"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are 
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""
