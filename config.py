import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ADMIN_ID = 6210355055
DATABASE_URL = os.getenv('DATABASE_URL')

# VPN Pricing
VPN_PRICING = {
    'monthly': 10,
    'yearly': 100
}

# Lottery Settings
LOTTERY_SETTINGS = {
    'ticket_price': 5,
    'draw_time': '2026-03-31 15:00:00'
}