# Trendyol İndirimli Ürünler Botu
Bu proje, Trendyol'da indirimli ürünleri bulur ve Telegram botu aracılığıyla gönderir.

## Kullanım

Telegram bot token'ınızı ve sohbet ID'nizi bot_token ve chat_id değişkenlerine ekleyin.

İndirimli ürünleri kontrol etmek istediğiniz Trendyol sayfasının URL'sini url değişkenine ekleyin.

Bot'u çalıştırmak için bot.py dosyasını çalıştırın.

python bot.py
Bot, belirtilen URL'deki indirimli ürünleri kontrol edecek ve yüzde 50'den büyük bir indirim varsa, ürün başlığı ve URL'si bot aracılığıyla size gönderilecektir.

## Gereksinimler
- Python 3.x
- requests kütüphanesi
- beautifulsoup4 kütüphanesi
- python-telegram-bot kütüphanesi
Gereksinimleri yüklemek için şu komutu çalıştırın:

pip install requests beautifulsoup4 python-telegram-bot
## Lisans
Bu proje, MIT lisansı altında lisanslanmıştır.
