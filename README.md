# git-commits-by-date
Git Commits by Date

```bash
git --no-pager log --shortstat --pretty=format:'%ad' --date=short \
| grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' \
| uniq -c \
| awk -v 'OFS=,' '{print $1,$2}' > daily_commits.csv
```
