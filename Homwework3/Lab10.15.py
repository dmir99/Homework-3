class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        percentage = self.team_wins / (self.team_wins + self.team_losses)
        return percentage


student_team = Team()
student_team.team_name = input()
student_team.team_wins = float(input())
student_team.team_losses = float(input())
number = student_team.get_win_percentage()


if number > 0.5:
    print("Congratulations, Team", student_team.team_name, "has a winning average!")
else:
    print("Team",student_team.team_name, "has a losing average.")





