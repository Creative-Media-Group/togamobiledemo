cd dist/
rm *
echo "DELETED"
cd ..
python3 -m briefcase create
python3 -m briefcase package -u
python3 -m briefcase create --target ubuntu:jammy
python3 -m briefcase package -u --target ubuntu:jammy