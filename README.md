# git-commits-by-date
Git commits by date

## Setup

```bash
pipenv shell
```

```bash
pipenv sync --dev
```

## Create daily_commits.csv

```bash
git --no-pager log --shortstat --pretty=format:'%ad' --date=short \
| grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' \
| uniq -c \
| awk -v 'OFS=,' '{print $1,$2}' > daily_commits.csv
```

## Create png

### plot

```bash
python run.py plot
```

### plot.png

<div align="left">
  <img src="images/plot.png">
</div>

### bar

```bash
python run.py bar
```

### bar.png

<div align="left">
  <img src="images/bar.png">
</div>
