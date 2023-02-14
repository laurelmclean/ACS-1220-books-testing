# Books App Part 4 (Tests)

## Running the Tests

**To run all of the tests**, you can run the following from the root project directory:

```
python3 -m unittest discover
```

(Make sure you have unittest installed.)

**To run all tests from a single file**, run the following:

```
python3 -m unittest books_app.main.tests
```

**To run one specific test**, you can run the following:

```
python3 -m unittest books_app.main.tests.MainTests.test_homepage_logged_in
```
