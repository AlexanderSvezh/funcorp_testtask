How to use:
1. Run Flask server (app.py)
2. Get curl request:

Example (subtraction):
```
curl -X POST 127.0.0.1:5000/calc/subtraction -d '{"x":11, "y": 0}' -H "Content-Type: application/json"
```

List of all methods:
(POST)
* /calc/addition
* /calc/subtraction
* /calc/multiply
* /calc/division

And two example methods for get/post request:
* /get (response example json from files/task.py)
* /post :)

3. Create 3-5 functional tests for all methods (pytest)
4. Find the bug :)
5. Write bug-report.
