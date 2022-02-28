echo "Publishing to test pypi"
flit publish --repository testpypi
echo "Publishing to production pypi"
flit publish
echo "Updating mirror repository"
& $PSScriptRoot\update-mirror.ps1
