pytest will run all files from current dir/subdirec test_*.py or*_test.py
we can run using "pytest" in the cmd

flags:
-x, --exitfirst       exit instantly on first error or failed test.

-r chars              show extra test summary info as specified by chars: (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed, (p)assed,
                        (P)assed with output, (a)ll except passed (p/P), or (A)ll. (w)arnings are enabled by default (see --disable-warnings),
                        'N' can be used to reset the list. (default: 'fE').


  --color=color         color terminal output (yes/no/auto).

  pytest -k test_api

-k EXPRESSION         only run tests which match the given substring expression. An expression is a python evaluatable expression where all
                    names are substring-matched against test names and their parent classes. Example: -k 'test_method or test_other' matches
                    all test functions and classes whose name contains 'test_method' or 'test_other', while -k 'not test_method' matches
                    those that don't contain 'test_method' in their names. -k 'not test_method and not test_other' will eliminate the
                    matches. Additionally keywords are matched to classes and functions containing extra names in their
                    'extra_keyword_matches' set, as well as functions which have names assigned directly to them. The matching is case-
                    insensitive.
