export GITHUB_TOKEN=$1
pip install --upgrade pip
pip install azure-ai-inference
pip install azure-core
mv main.py l2l
chmod +x l2l
mv l2l $PREFIX/bin
echo "Done!"
