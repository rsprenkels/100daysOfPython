from unittest import mock
from io import StringIO
from sys import stdout

class Acm:

    def run():
        fields = input().split(); time = int(fields[0])
        logsPerProblem = {}

        while (time >= 0):
            problemID = fields[1]
            result = fields[2]
            if (problemID not in logsPerProblem):
                logsPerProblem[problemID] = []
            logsPerProblem[problemID].append([time, result])
            fields = input().split(); time = int(fields[0])

        timeMeasure = 0 
        solvedCorrectly = 0
        for problemID, logList in logsPerProblem.items():
            if (logList[-1][1] == 'right'):
                solvedCorrectly += 1
                timeForThisProblem = logList[-1][0] + (len(logList) - 1) * 20
                timeMeasure += timeForThisProblem
                # print("prob {}  at {} thisTime {} totalTime {}".format(problemID, logList[-1][0], timeForThisProblem, timeMeasure))
        print("{} {}".format(solvedCorrectly, timeMeasure))


@mock.patch('sys.stdout', new_callable=StringIO)
def test_1(mock_stdout):
    user_input      = [ 
           '7 H right',
           '15 B wrong',
           '30 E wrong',
           '35 E right',
           '80 B wrong',
           '80 B right',
           '100 D wrong',
           '100 C wrong',
           '300 C right',
           '300 D wrong',
           '-1'
       ]
    expected_output = ['4 502']
    with mock.patch('builtins.input', side_effect=user_input):
        Acm.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

@mock.patch('sys.stdout', new_callable=StringIO)
def test_2(mock_stdout):
    user_input      = [ 
           '3 E right',
           '10 A wrong',
           '30 C wrong',
           '50 B wrong',
           '100 A wrong',
           '200 A right',
           '250 C wrong',
           '300 D right',
           '-1'
       ]
    expected_output = ['3 543']
    with mock.patch('builtins.input', side_effect=user_input):
        Acm.run()
        assert mock_stdout.getvalue() == '\n'.join(expected_output) + '\n'

if __name__ == '__main__':
    Acm.run()

