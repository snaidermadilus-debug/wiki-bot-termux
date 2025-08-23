pkg update && pkg upgrade -y
pkg install git python termux-api -y
pip install wikipedia

git clone https://github.com/snaidermadilus-debug/wiki-bot-termux.git
cd wiki-bot-termux

python wiki_bot.py