curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $3"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/$1/$2/pulls \
  -d '{"title":"Replace magic number","body":"Converted the group ids into an array","head":"week2_pr","base":"week2"}'
