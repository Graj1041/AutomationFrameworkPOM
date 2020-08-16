pytest -v -s --html=./Reports/report.html testCases/test_Home.py --browser chrome

REM pytest -v -s -m "sanity" --html=./Reports/report.html testCases/ --browser firefox

REM pytest -v -s -m "feature" --html=./Reports/report.html testCases/ --browser safari