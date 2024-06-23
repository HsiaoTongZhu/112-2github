import csv
import os
import random

# 確認檔案路徑
file_path = 'pe8_data.csv'

# 檢查檔案是否存在
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"找不到檔案或路徑: '{file_path}'")

teams = []

# 讀取 CSV 檔案
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # 跳過標題列
    for row in reader:
        # 檢查列長度是否正確，跳過空行
        if len(row) < 9 or not row[0]:
            continue
        teams.append(row)

# (1) 東區哪些球隊的主場勝率低於客場勝率
def get_win_percentage(record):
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)

eastern_teams = [team for team in teams if team[0] == 'Eastern']
teams_home_lower_than_away = []

for team in eastern_teams:
    home_pct = get_win_percentage(team[7])
    away_pct = get_win_percentage(team[8])
    if home_pct < away_pct:
        teams_home_lower_than_away.append(team[1])

print("東區主場勝率低於客場勝率的球隊:")
print(teams_home_lower_than_away)

# (2) 哪一區的球隊擁有較高的“平均得分減掉失分”
pf_pa_diff = {'Eastern': [], 'Western': []}

for team in teams:
    conference = team[0]
    pf = float(team[5])  # 使用 float 處理浮點數
    pa = float(team[6])
    pf_pa_diff[conference].append(pf - pa)

avg_pf_pa_diff = {conf: sum(diffs) / len(diffs) for conf, diffs in pf_pa_diff.items()}
higher_avg_conference = max(avg_pf_pa_diff, key=avg_pf_pa_diff.get)

print("\n得分減去失分平均值較高的區:")
print(higher_avg_conference)

# (3) 根據每支球隊和另一區球隊的對戰記錄來對所有球隊排序
# 假設 CSV 檔案中有一欄“Inter-Conference”表示對另一區的表現
# 這裡我們創建一個示例“Inter-Conference”勝率數據

# 如果沒有“Inter-Conference”數據，創建模擬數據
for team in teams:
    team.append(random.random())  # 模擬對另一區的勝率

# 確保勝率數據為浮點數
for team in teams:
    team[9] = float(get_win_percentage(team[9]))  # 將勝率轉換為浮點數

# 排序球隊根據對另一區的勝率
teams.sort(key=lambda x: x[9], reverse=True)

ranking = [(team[1], team[9]) for team in teams]

print("\n根據對另一區表現排序的所有球隊排名:")
for rank, (team_name, inter_conf_pct) in enumerate(ranking, start=1):
    print(f"{rank}. {team_name} - 勝率: {inter_conf_pct:.2f}")
