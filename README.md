git clone https://github.com/Jonna1976/anchoring-examples.git
cd anchoring-examples
# Kopieer de README die we gemaakt hebben
cp ~/umarise/docs/anchoring-examples-README.md README.md

# Maak example folders
mkdir -p examples/ci examples/ai examples/data examples/release

# Anchor een testbestand
echo "hello world" > examples/ci/build-output.tar.gz
npx @umarise/cli anchor examples/ci/build-output.tar.gz

git add .
git commit -m "Initial examples with .proof files"
git push
