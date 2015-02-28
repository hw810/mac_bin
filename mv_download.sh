cd ~/Downloads/
ls -lth | head -2 | tail -n+2 | awk '{print $9 }' | xargs -I {} mv {}  ~/Desktop/
cd 
