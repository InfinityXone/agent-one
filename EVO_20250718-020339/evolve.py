import os, json, shutil, datetime, subprocess

def evolve():
    now = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    base = os.getcwd().split(os.sep)[-1].split('_')[0]
    newp = f"{base}_{now}"
    os.makedirs(newp, exist_ok=True)
    for f in ['start.md', 'manifest.json', os.path.basename(__file__)]:
        shutil.copy(f, os.path.join(newp, f))
    subprocess.Popen(['python', os.path.join(newp, os.path.basename(__file__))])

if __name__ == '__main__':
    evolve()
