export GITHUB_TOKEN=$(cat gtoken.env)
pip install azure-ai-inference
pip install azure-core
mv main.py l2l
chmod +x l2l
mv l2l $PREFIX/bin
echo "Done!"
