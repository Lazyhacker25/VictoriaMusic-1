import time
from datetime import datetime
@Client.on_message(filters.command('ping', '!'))
async def ping_msg_handler(_, m: Message):
    to_be_edited = await m.reply('Pinging..')
    start_ms = datetime.now()
    uptime = get_readable_time((time.time() - StartTime))
    end = datetime.now()
    ms = (end - start_ms).microseconds / 1000
    calls_ping = await group_calls.ping
    await to_be_edited.edit('🏓 Pong\n⟶ ms: {}\n⟶ PyTgCalls ping: {}\n⟶ Uptime: {}'.format(ms, round(calls_ping, 2), uptime))
