import time
from datetime import datetime
import os
from os import path
from typing import Callable

import aiofiles
import aiohttp
import ffmpeg
import requests
import wget
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Python_ARQ import ARQ
from youtube_search import YoutubeSearch

from VictoriaMusic.config import ARQ_API_KEY
from VictoriaMusic.config import BOT_NAME as bn
from VictoriaMusic.config import DURATION_LIMIT
from VictoriaMusic.config import UPDATES_CHANNEL as updateschannel
from VictoriaMusic.config import que
from VictoriaMusic.function.admins import admins as a
from VictoriaMusic.helpers.admins import get_administrators
from VictoriaMusic.helpers.channelmusic import get_chat_id
from VictoriaMusic.helpers.decorators import authorized_users_only
from VictoriaMusic.helpers.filters import command, other_filters
from VictoriaMusic.helpers.gets import get_file_name
from VictoriaMusic.services.callsmusic import callsmusic
from VictoriaMusic.services.callsmusic import client as USER
from VictoriaMusic.services.converter.converter import convert
from VictoriaMusic.services.downloaders import youtube
from VictoriaMusic.services.queues import queues

@Client.on_message(filters.command('ping', '!'))
async def ping_msg_handler(_, m: Message):
    to_be_edited = await m.reply('Pinging..')
    start_ms = datetime.now()
    uptime = get_readable_time((time.time() - StartTime))
    end = datetime.now()
    ms = (end - start_ms).microseconds / 1000
    calls_ping = await group_calls.ping
    await to_be_edited.edit('🏓 Pong\n⟶ ms: {}\n⟶ PyTgCalls ping: {}\n⟶ Uptime: {}'.format(ms, round(calls_ping, 2), uptime))
