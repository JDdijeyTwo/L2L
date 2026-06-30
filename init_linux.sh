export GITHUB_TOKEN="$1"
pip install azure-ai-inference
pip install azure-core
mv main.py l2l
chmod +x l2l
mv l2l /usr/local/bin
echo "Done! (for linux)"
#linux users, I VERY LOVE YOU
