shopt -s expand_aliases
source ~/.bashrc
source ~/.bash_aliases
source ~/.bash_profile
passmepass="$GITHUB_ACCESS_TOKEN_COMMANDLINE"
github_password=":""$passmepass""@"

# Clone repositories
cat README.md |  awk -F '(' '{print $2}' | awk -F ')**' '{print $1}' | sort -u | while read repository
do
	if [ ! -z "$repository" ]; then
		git clone `echo "$repository"".git" | sed s/'github.com'/'machineydv:@github.com'/g | sed s/':@'/$github_password/g`
	fi
done

gitpass
mkdir "My-Binaries"
