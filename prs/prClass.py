import datetime

class ExercisePRs:
    def __init__(self, ex_name, prs_data):
        self.ex_name = ex_name
        self.data = self.parse_pr_data(prs_data)

    def __str__(self):
        st = f"{self.ex_name}\n"
        for datapoint in self.data:
            st += f"Weight: {datapoint.get('weight') + ' kg' :12s}"
            st += f"Reps: {datapoint.get('reps'):8s}"
            st += f"Date: {datapoint.get('date')}\n"

        return st


    def parse_pr_data(self, prs_data):
        return [{"weight": datapoint[0],
                 "reps": datapoint[1],
                 "date": datapoint[2]} # TODO NOG NAAR  DATETIME ZETTEN
                 for datapoint in prs_data]
