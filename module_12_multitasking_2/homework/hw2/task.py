import subprocess
import pandas as pd


def process_count(username: str) -> int:
    a = subprocess.run(["ps", "-aux", "--sort", "-rss"], stdout=subprocess.PIPE)
    data = str(a.stdout.decode('utf-8'))
    df = pd.DataFrame([x.split() for x in data.splitlines()])
    df.columns = df.iloc[0]
    a=df[df['USER'] == username].shape[0]
    return a
process_count('george')



def total_memory_usage(root_pid: int) -> int:
    a = subprocess.run(["ps", "-aux", "--sort", "-rss"], stdout=subprocess.PIPE)
    data = str(a.stdout.decode('utf-8'))
    df = pd.DataFrame([x.split() for x in data.splitlines()])
    df.columns = df.iloc[0]
    a = df[df['PID'] == str(root_pid)]['RSS'].sum()
    return a
total_memory_usage(2625)
