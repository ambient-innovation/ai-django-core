echo "Changing directory"
cd ..
echo "Entering mirror directory"
cd ai-django-core-mirror
echo "Fetching branches from upstream"
git fetch upstream
echo "Merging master"
git merge upstream/master
echo "Pushing changes to mirror"
git push
echo "Changing directory back"
cd ../ai-django-core
