class script(object):
    START_TXT = """𝗛𝗶 {},
𝖨 𝖺𝗆 𝗃𝗎𝗌𝗍 𝖺 𝗌𝗂𝗆𝗉𝗅𝖾 𝗉𝗋𝖾 - 𝖿𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝖾𝖽 𝖺𝗎𝗍𝗈𝖿𝗂𝗅𝗍𝖾𝗋 𝖻𝗈𝗍

𝗂𝗍𝗌 𝗌𝗂𝗆𝗉𝗅𝖾 𝗍𝗈 𝗎𝗌𝖾 𝗆𝖾:- 𝗃𝗎𝗌𝗍 𝖺𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 𝖺𝗌 𝖺𝖽𝗆𝗂𝗇, 𝗍𝗁𝖺𝗍𝗌 𝖺𝗅𝗅 𝗂 𝗐𝗂𝗅𝗅 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝗆𝗈𝗏𝗂𝖾𝗌 𝗍𝗁𝖾𝗋𝖾. /help 𝖿𝗈𝗋 𝗆𝗈𝗋𝖾 𝗂𝗇𝖿𝗈..."""
    HELP_TXT = """
<b>𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:-</b> 
/start - 𝖼𝗁𝖾𝖼𝗄 𝗐𝗁𝖾𝗍𝗁𝖾𝗋 𝗂𝗆 𝗈𝗇𝗅𝗂𝗇𝖾 
/help - 𝗀𝖾𝗍 𝗍𝗁𝗂𝗌 𝗁𝖾𝗅𝗉 𝗆𝖾𝗌𝗌𝖺𝗀𝖾
/about - 𝖺𝖻𝗈𝗎𝗍 𝗆𝖾"""
    ABOUT_TXT = """
○ 𝖬𝗒 𝖭𝖺𝗆𝖾 : <a href=https://t.me/{}>{}</a>
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href="https://t.me/DARKWEBLOAD">𝑡ℎ𝑖𝑠 𝑝𝑒𝑟𝑠𝑜𝑛</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥 
○ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆
○ 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖧𝖾𝗋𝗈𝗄𝗎
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : 𝖬𝗈𝗇𝗀𝗈𝖣𝖡 
○ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : 𝖵9.8 [BeTa]"""

    DONATION_TXT = """<b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 & 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b> 

›› <b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━

›› <b>𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━"""
    PROMOTION_TXT = """<b>〄 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 〄</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━"""
    ALIVE_TXT ="""<b>ALIVE MODULE</b>
• /alive - check me alive or dead🤧
Just for a rasam😂"""
    INFO_TXT = """Help: <b>Information</b>
Get information about something!
<b>Commands and Usage:</b>
• /id - get id of a specifed user.
• /info  - get information about a user.
• /json - get the json details of a message.
<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    FILE_TXT = """𝗛𝗲𝗹𝗽 : 𝗳𝗶𝗹𝗲 𝘀𝘁𝗼𝗿𝗲 𝗺𝗼𝗱𝘂𝗹𝗲..

𝖡𝗒 𝗎𝗌𝗂𝗇𝗀 𝗍𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝗒𝗈𝗎 𝖼𝖺𝗇 𝗌𝗍𝗈𝗋𝖾 𝖿𝗂𝗅𝖾𝗌 𝗂𝗇 𝗆𝗒 𝖽𝖺𝗍𝖺 𝖻𝖺𝗌𝖾 𝖺𝗇𝖽 𝗂 𝗐𝗂𝗅𝗅 𝗀𝗂𝗏𝖾 𝗒𝗈𝗎 𝖺 𝗉𝖾𝗋𝗆𝖾𝗇𝖾𝗇𝗍 𝗅𝗂𝗇𝗄 𝗍𝗈 𝖺𝖼𝖼𝖾𝗌𝗌 𝗍𝗁𝖾 𝗌𝖺𝗏𝖾𝖽 𝖿𝗂𝗅𝖾𝗌. 𝗂𝖿 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝖺𝖽𝖽 𝖿𝗂𝗅𝖾𝗌 𝖿𝗋𝗈𝗆 𝖺 𝗉𝗋𝗂𝗏𝖺𝗍𝖾 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗒𝗈𝗎 𝗆𝗎𝗌𝗍 𝗆𝖺𝗄𝖾 𝗆𝖾 𝖺𝖽𝗆𝗂𝗇 𝗈𝗇 𝗍𝗁𝖾 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 𝗍𝗈 𝖺𝖼𝖼𝖾𝗌𝗌 𝖿𝗂𝗅𝖾𝗌...

» 𝗖𝗼𝗺𝗺𝗮𝗻𝘁𝘀 𝗮𝗻𝗱 𝘂𝘀𝗮𝗴𝗲 :

• /plink ›› 𝗋𝖾𝗉𝗅𝖺𝗒 𝗍𝗈 𝖺𝗇𝗒 𝗆𝖾𝖺𝖽𝗂𝖺 𝗍𝗈 𝗀𝖾𝗍 𝗅𝗂𝗇𝗄.
• /pbatch ›› 𝗎𝗌𝖾 𝗒𝗈𝗎𝗋 𝗆𝖾𝖺𝖽𝗂𝖺 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽.
• /batch ›› 𝗍𝗈 𝖼𝗋𝖾𝖺𝗍 𝗅𝗂𝗇𝗄𝗌 𝖿𝗈𝗋 𝗆𝗎𝗅𝗍𝗂𝗉𝗅𝖾 𝖿𝗂𝗅𝖾𝗌.

• 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 » <code>
/batch   https://t.me/+Rc9TK3wIf6xjODE9</code>

𝖢𝗋𝖾𝖽𝗂𝗍𝗌 ›› <a href=https://t.me/DARKWEBLOAD><b>Dᴀʀᴋ ᴡᴇʙʟᴏᴀᴅ🇮🇳</b></a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>〽️ 𝖩𝗎𝗌𝗍 𝖲𝗎𝗆 𝖪𝗂𝗇𝖽 𝖮𝖿 𝖥𝗎𝗇 𝖳𝗁𝗂𝗇𝗀'𝗌 〽️</b>
 
𝟣. /dice - 𝖱𝗈𝗅𝖾 𝖳𝗁𝖾 𝖣𝗂𝗌𝖾
𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 𝖣𝖺𝗋𝗍 
3. /Runs - 𝖲𝗈𝗆𝖾 𝖱𝖺𝗇𝖽𝗈𝗆 𝖣𝗂𝖺𝗅𝗈𝗀𝖾𝗌 
4. /Goal or /Shoot - 𝖳𝗈 𝖬𝖺𝗄𝖾 𝖠 𝖦𝗈𝖺𝗅 𝖮𝗋 𝖲𝗁𝗈𝗈𝗍
5. /luck or /cownd - 𝖲𝗉𝗂𝗇 𝖠𝗇𝖽 𝖳𝗋𝗒 𝖸𝗈𝗎𝗋 𝖫𝗎𝖼𝗄"""

    MANUELFILTER_TXT = """Help: <b>𝖥𝗂𝗅𝗍𝖾𝗋𝗌</b>

- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>

1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    SONG_TXT = """<b>𝖲𝗈𝗇𝗀 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖬𝗈𝖽𝗎𝗅𝖾</b>

<b>𝖲𝗈𝗇𝗀 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖬𝗈𝖽𝗎𝗅𝖾, 𝖥𝗈𝗋 𝖳𝗁𝗈𝗌𝖾 𝖶𝗁𝗈 𝖫𝗈𝗏𝖾 𝖬𝗎𝗌𝗂𝖼. 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖥𝗈𝗋 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖬𝗎𝗌𝗂𝖼. 𝖠𝗇𝗒 𝖲𝗈𝗇𝗀 𝖶𝗂𝗍𝗁 𝖲𝗎𝗉𝖾𝗋 𝖥𝖺𝗌𝗍 𝖲𝗉𝖾𝖾𝖽.𝖶𝗈𝗋𝗄𝗌 𝖮𝗇𝗅𝗒 𝖮𝗇 𝖦𝗋𝗈𝗎𝗉..</b>

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌</b>

››  /song 𝖲𝗈𝗇𝗀 𝖭𝖺𝗆𝖾 

𝖶𝗈𝗋𝗄𝗌 𝖮𝗇𝗅𝗒 𝖮𝗇 𝖦𝗋𝗈𝗎𝗉

𝖢𝗋𝖾𝖽𝗂𝗍𝗌 :- <a href=https://t.me/DARKWEBLOAD>Dᴀʀᴋ ᴡᴇʙʟᴏᴀᴅ🇮🇳</a>"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>𝖯𝗂𝗇 𝖠 𝖬𝖺𝗌𝗌𝖺𝗃𝖾..</b>

<b>𝖠𝗅𝗅 𝖳𝗁𝖾 𝖯𝗂𝗇 𝖬𝖺𝗌𝗌𝖺𝗀𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖢𝖺𝗇 𝖡𝖾 𝖥𝗈𝗎𝗇𝖽 𝖧𝖾𝗋𝖾 :</b>

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾𝗌</b>

◉ /pin :- 𝖳𝗈 𝖯𝗂𝗇 𝖳𝗁𝖾 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖮𝗇 𝖸𝗈𝗎𝗋 𝖢𝗁𝖺𝗍𝗌
◉ /unpin :- 𝖳𝗈 𝖴𝗇𝗉𝗂𝗇 𝖳𝗁𝖾 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖯𝗂𝗇𝗇𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾"""
    SEARCH_TXT = """Help: <b>IMDb</b>
Search many things without leaving telegram!
<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.
<b>NOTE:</b>
• IMDb should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""
    PASTE_TXT = """Help: <b>Paste</b>

𝖯𝖺𝗌𝗍𝖾 𝖲𝗈𝗆𝖾 𝖳𝖾𝗑𝗍𝗌 𝖮𝗋 𝖣𝗈𝖼𝗎𝗆𝖾𝗍𝗌 𝖮𝗇 𝖠 𝖶𝖾𝖻𝗌𝗂𝗍𝖾!

<b>Commands and Usage:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• 𝖳𝗁𝖾𝗌𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖶𝗈𝗋𝗄𝗌 𝖮𝗇 𝖡𝗈𝗍𝗁 𝖯𝗆 𝖠𝗇𝖽 𝖦𝗋𝗈𝗎𝗉.
• 𝖳𝗁𝖾𝗌𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖢𝖺𝗇 𝖡𝖾 𝖴𝗌𝖾𝖽 𝖡𝗒 𝖠𝗇𝗒 𝖦𝗋𝗈𝗎𝗉 𝖬𝖾𝗆𝖻𝖾𝗋."""
    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝖳𝖾𝗑𝗍 𝖳𝗈 𝖲𝗉𝖾𝖾𝖼𝗁

<b>Commands and Usage:</b>

• /tts <text> : 𝖢𝗈𝗇𝗏𝖾𝗋𝗍 𝖳𝖾𝗑𝗍 𝖳𝗈 𝖲𝗉𝖾𝖾𝖼𝗁

<b>NOTE:</b>

• 𝖨𝗆𝖽𝖻 𝖲𝗁𝗈𝗎𝗅𝖽 𝖧𝖺𝗏𝖾 𝖠𝖽𝗆𝗂𝗇 𝖯𝗋𝖾𝗏𝗂𝗅𝖺𝗀𝖾.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>🔗 𝖯𝗂𝗇𝗀:</b>

Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

• /alive - To check you are alive.
• /ping - To get your ping.

<b>👨‍💻 Usage:</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

𝖤𝗏𝖾𝗋𝗂𝗒𝗈𝗇𝖾 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 , 𝖨𝖿 𝖲𝗉𝖺𝗆𝗂𝗇𝗀 𝖧𝖺𝗉𝗉𝖾𝗇 𝖡𝗈𝗍 𝖶𝗂𝗅𝗅 𝖠𝗎𝗍𝗈𝗆𝖺𝗍𝗂𝖼𝖺𝗅𝗅𝗒 𝖡𝖺𝗇 𝖸𝗈𝗎 𝖥𝗋𝗈𝗆 𝖳𝗁𝖾 𝖦𝗋𝗈𝗎𝗉."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+Rc9TK3wIf6xjODE9)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖮𝗇/𝖮𝖿𝖿 𝖬𝗈𝖽𝗎𝗅𝖾..</b>

<b>𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖨𝗌 𝖳𝗁𝖾 𝖥𝖾𝖺𝗍𝗎𝗋𝖾 𝖳𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖠𝗇𝖽 𝖲𝖺𝗏𝖾 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾𝗌 𝖠𝗎𝗍𝗈𝗆𝖺𝗍𝗂𝖼𝖺𝗅𝗅𝗒 𝖥𝗋𝗈𝗆 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 𝖳𝗈 𝖦𝗋𝗈𝗎𝗉. 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖳𝗁𝖾 𝖥𝗈𝗅𝗅𝗐𝗂𝗇𝗀 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖳𝗈 𝖮𝗇 𝖠𝗇𝖽 𝖮𝖿𝖿 𝖳𝗁𝖾 𝖠𝗎𝗍𝗈𝖥𝗂𝗅𝗍𝖾𝗍 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉.../</b>

<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 :-
<b>›› /autofilter on - 𝖤𝗇𝖺𝖻𝗅𝖾 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖨𝗇 𝗍𝗁𝖾 𝖦𝗋𝗈𝗎𝗉.</b>
<b>›› /autofilter off - 𝖣𝗂𝗌𝖺𝖻𝗅𝖾𝖽 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋 𝖨𝗇 𝗍𝗁𝖾 𝖦𝗋𝗈𝗎𝗉.</b>
<b>›› /set_template - 𝖲𝖾𝗍 𝖢𝗎𝗌𝗍𝗈𝗆 𝖨𝗆𝖽𝖻 𝖳𝖾𝗆𝗉𝗅𝖺𝗍𝖾 𝖥𝗈𝗋 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋.</b>
<b>›› /get_template - 𝖦𝖾𝗍 𝖢𝗎𝗋𝗋𝖾𝗇𝗍 𝖨𝗆𝖽𝖻 𝖳𝖾𝗆𝗉𝗅𝖺𝗍𝖾 𝖮𝖿 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋.</b>

<b>𝖢𝗋𝖾𝖽𝗂𝗍𝗌 :- <a href=https://t.me/DARKWEBLOAD>Dᴀʀᴋ ᴡᴇʙʟᴏᴀᴅ🇮🇳</a></b>"""
    CONNECTION_TXT = """Help: <b>𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇𝗌</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>𝖤𝗑𝗍𝗋𝖺 𝖬𝗈𝖽𝗎𝗅𝖾𝗌</b>

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban_user  - <code>to ban a user.</code>
• /unban_user  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>🗃️ 𝖳𝗈𝗍𝖺𝗅 𝖥𝗂𝗅𝖾𝗌 : <code>{}</code></b>
<b>👤 𝖳𝗈𝗍𝖺𝗅 𝖴𝗌𝖾𝗋𝗌 : <code>{}</code></b>
<b>👥 𝖳𝗈𝗍𝖺𝗅 𝖢𝗁𝖺𝗍𝗌 : <code>{}</code></b>
<b>💾 𝖴𝗌𝖾𝖽 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 : <code>{}</code> 𝖬𝖻</b>
<b>🖥️ 𝖥𝗋𝖾𝖾 𝖲𝗍𝗈𝗋𝖺𝗀𝖾 : <code>{}</code> 𝖬𝖻</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>♻️ 𝖦𝗋𝗈𝗎𝗉 ⪼ {}(<code>{}</code>)</b>
<b>👨‍👨‍👧‍👦 𝖳𝗈𝗍𝖺𝗅 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 ⪼ <code>{}</code></b>
<b>👨‍💻 𝖠𝖽𝖽𝖾𝖽 𝖡𝗒 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝖨𝖽 - <code>{}</code></b>
<b>᚛› 𝖭𝖺𝗆𝖾 - {}</b>
"""
    REPORT_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖱𝖾𝗉𝗈𝗋𝗍 ⚠️

𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖱𝖾𝗉𝗈𝗋𝗍 𝖠 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖮𝗋 𝖠 𝖴𝗌𝖾𝗋 𝖳𝗈 𝖳𝗁𝖾 𝖠𝖽𝗆𝗂𝗇 𝖮𝖿 𝖳𝗁𝖾 𝖱𝖾𝗌𝗉𝖾𝖼𝗍𝗂𝗏𝖾 𝖦𝗋𝗈𝗎𝗉. 𝖣𝗈𝗇'𝗍 𝖬𝗂𝗌𝗎𝗌𝖾 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽.

➤ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:

➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""

    CORONA_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖢𝗈𝗏𝗂𝖽

𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖧𝖾𝗅𝗉𝗌 𝖸𝗈𝗎 𝖳𝗈 𝖪𝗇𝗈𝗐 𝖣𝖺𝗂𝗅𝗒 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖠𝖻𝗈𝗎𝗍 𝖢𝗈𝗏𝗂𝖽 

➤ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖴𝗌𝖺𝗀𝖾:

➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>"""

    URLSHORT_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖲𝗁𝗈𝗋𝗍 𝖠 𝖴𝗋𝗅 

➤ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/IF_qoYnCLjs</code>"""

    VIDEO_TXT ="""𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖵𝗂𝖽𝖾𝗈𝗌 𝖥𝗋𝗈𝗆 𝖸𝗈𝗎𝗍𝗎𝖻𝖾.

• 𝖴𝗌𝖺𝗀𝖾
𝗒𝗈𝗎 𝖼𝖺𝗇 𝖽𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖺𝗇𝗒 𝗏𝗂𝖽𝖾𝗈 𝖿𝗋𝗈𝗆 𝗒𝗈𝗎𝗍𝗎𝖻𝖾

𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾
• 𝖳𝗒𝗉𝖾 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/IF_qoYnCLjs)
• 𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/mp4 https://youtu.be/IF_qoYnCLjs</code>
<code>/video https://youtu.be/IF_qoYnCLjs</code>"""

    ZOMBIES_TXT = """𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖪𝗂𝖼𝗄 𝖴𝗌𝖾𝗋

<b>𝖪𝗂𝖼𝗄 𝖨𝗇𝖺𝖼𝗍𝗂𝗏𝖾 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 𝖥𝗋𝗈𝗆 𝖦𝗋𝗈𝗎𝗉. 𝖠𝖽𝖽 𝖬𝖾 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇 𝖶𝗂𝗍𝗁 𝖡𝖺𝗇 𝖴𝗌𝖾𝗋𝗌 𝖯𝖾𝗋𝗆𝗂𝗌𝗎𝗈𝗇 𝖨𝗇 𝖦𝗋𝗈𝗎𝗉.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝖧𝖾𝗅𝗉 : 𝖨𝗆𝖺𝗀𝖾

𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖤𝖽𝗂𝗍 𝖨𝗆𝖺𝗀𝖾 𝖵𝖾𝗋𝗒 𝖤𝖺𝗌𝗂𝗅𝗒 

➤ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:

➪ 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨

𝖬𝖺𝖽𝖾 𝖡𝗒 <a href=https://t.me/DARKWEBLOAD>Dᴀʀᴋ ᴡᴇʙʟᴏᴀᴅ🇮🇳</a>"""

    STICKER_TXT = """𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖳𝗁𝗂𝗌 𝖬𝗈𝖽𝗎𝗅𝖾 𝖳𝗈 𝖥𝗂𝗇𝖽 𝖠𝗇𝗒 𝖲𝗍𝗂𝖼𝗄𝖾𝗋𝗌 𝖨𝖽.
• 𝖴𝗌𝖺𝗀𝖾
To Get Sticker ID
 
  🛃 𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾
 
◉ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """𝖧𝖾𝗅𝗉𝗌 𝖳𝗈 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽 𝖠𝗇𝗒 𝖸𝗈𝗎𝗍𝗎𝖻𝖾 𝖵𝗂𝖽𝖾𝗈 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅
    
🛃 𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾
𝖳𝗒𝗉𝖾 /ytthumb 𝖠𝗇𝖽 𝖵𝗂𝖽𝖾𝗈 𝖫𝗂𝗇𝗄

• 𝖤𝗑𝖺𝗆𝗉𝗅𝖾
<code>/ytthumb https://youtu.be/OWqbMNrVt5s</code>"""

    ABOOK_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄

𝖸𝗈𝗎 𝖢𝖺𝗇 𝖢𝗈𝗇𝗏𝖾𝗋𝗍 𝖠 𝖯𝖽𝖿 𝖥𝗂𝗅𝖾 𝖳𝗈 𝖠 𝖵𝗂𝖽𝖾𝗈 𝖥𝗂𝗅𝖾 𝖶𝗂𝗍𝗁 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽.

➤𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖠𝗇𝖽 𝖴𝗌𝖺𝗀𝖾:

➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋

𝖳𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝖧𝖾𝗅𝗉 𝖸𝗈𝗎 𝖳𝗈 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾 𝖠 𝖳𝖾𝗑𝗍 𝖳𝗈 𝖠𝗇𝗒 𝖫𝖺𝗇𝗀𝗎𝗀𝖾𝗌 𝖨𝖿 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍. 𝖳𝗁𝗂𝗌 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 𝖶𝗈𝗋𝗄𝗌 𝖮𝗇 𝖡𝗈𝗍𝗁 𝖯𝗆 𝖠𝗇𝖽 𝖦𝗋𝗈𝗎𝗉.

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    RESTRIC_TXT = """➤ 𝖧𝖾𝗅𝗉: 𝖬𝗎𝗍𝖾 🚫

𝖳𝗁𝖾𝗌𝖾 𝖠𝗋𝖾 𝖳𝗁𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖠 𝖦𝗋𝗈𝗎𝗉 𝖠𝖽𝗆𝗂𝗇 𝖢𝖺𝗇 𝖳𝗈 𝖬𝖺𝗌𝗌𝖺𝗀𝖾 𝖳𝗁𝗂𝖾𝗋 𝖦𝗋𝗈𝗎𝗉 𝖬𝗈𝗋𝖾 𝖤𝖿𝖿𝗂𝖼𝗂𝗇𝗍𝗅𝗒.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    CREATOR_REQUIRED = """❗<b>𝖸𝗈𝗎 𝖧𝖺𝗏𝖾 𝖳𝗈 𝖡𝖾 𝖳𝗁𝖾 𝖦𝗋𝗈𝗎𝗉 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 𝖳𝗈 𝖣𝗈 𝖳𝗁𝖺𝗍.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
