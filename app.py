import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

API_TOKEN = '362503576:AAEtAY00_17I3GjUXIAe4Btl_L4CUFOIsGI'
WEBHOOK_URL = 'https://a7702364.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'taiwan',
        'taiwan_trending',
        'taiwan_travel',
        'taiwan_news',
        'taiwan_music',
        'america',
        'america_trending',
        'america_travel',
        'america_news',
        'america_music',
        'hongkong',
        'hongkong_trending',
        'hongkong_travel',
        'hongkong_news',
        'hongkong_music',
        'finish_state'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'taiwan',
            'conditions': 'is_going_to_taiwan'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'america',
            'conditions': 'is_going_to_america'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'hongkong',
            'conditions': 'is_going_to_hongkong'
        },
        {
            'trigger': 'taiwan_advance',
            'source': 'taiwan',
            'dest': 'taiwan_trending',
            'conditions': 'is_going_to_taiwan_trending'
        },
        {
            'trigger': 'taiwan_advance',
            'source': 'taiwan',
            'dest': 'taiwan_travel',
            'conditions': 'is_going_to_taiwan_travel'
        },
        {
            'trigger': 'taiwan_advance',
            'source': 'taiwan',
            'dest': 'taiwan_news',
            'conditions': 'is_going_to_taiwan_news'
        },
        {
            'trigger': 'taiwan_advance',
            'source': 'taiwan',
            'dest': 'taiwan_music',
            'conditions': 'is_going_to_taiwan_music'
        },
        {
            'trigger': 'america_advance',
            'source': 'america',
            'dest': 'america_trending',
            'conditions': 'is_going_to_america_trending'
        },
        {
            'trigger': 'america_advance',
            'source': 'america',
            'dest': 'america_travel',
            'conditions': 'is_going_to_america_travel'
        },
        {
            'trigger': 'america_advance',
            'source': 'america',
            'dest': 'america_news',
            'conditions': 'is_going_to_america_news'
        },
        {
            'trigger': 'america_advance',
            'source': 'america',
            'dest': 'america_music',
            'conditions': 'is_going_to_america_music'
        },
        {
            'trigger': 'hongkong_advance',
            'source': 'hongkong',
            'dest': 'hongkong_trending',
            'conditions': 'is_going_to_hongkong_trending'
        },
        {
            'trigger': 'hongkong_advance',
            'source': 'hongkong',
            'dest': 'hongkong_travel',
            'conditions': 'is_going_to_hongkong_travel'
        },
        {
            'trigger': 'hongkong_advance',
            'source': 'hongkong',
            'dest': 'hongkong_news',
            'conditions': 'is_going_to_hongkong_news'
        },
        {
            'trigger': 'hongkong_advance',
            'source': 'hongkong',
            'dest': 'hongkong_music',
            'conditions': 'is_going_to_hongkong_music'
        },
        {
            'trigger': 'finish',
            'source': [
                'taiwan_trending',
                'taiwan_travel',
                'taiwan_news',
                'taiwan_music',
                'america_trending',
                'america_travel',
                'america_news',
                'america_music',
                'hongkong_trending',
                'hongkong_travel',
                'hongkong_news',
                'hongkong_music'
            ],
            'dest': 'finish_state'
        },
        {
            'trigger': 'go_back',
            'source': 'finish_state',
            'dest': 'user'
        }

    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print('From client: ' + update.message.text)
    print(machine.currentState)
    print(machine.first_visit)
    if machine.first_visit == 0:
        update.message.reply_text("Please Choose a Region:\nTaiwan\nAmerica\nHongkong\n")
    if machine.currentState == 'user':
        machine.advance(update)
    if machine.currentState == 'taiwan':
        machine.taiwan_advance(update)
    if machine.currentState == 'america':
        machine.america_advance(update)
    if machine.currentState == 'hongkong':
        machine.hongkong_advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

if __name__ == "__main__":
    _set_webhook()
    app.run()
