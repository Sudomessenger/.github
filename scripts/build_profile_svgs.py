"""Generate all branded SVG panels for the Sudomessenger org profile.

Run from repo root:
    python3 scripts/build_profile_svgs.py
"""
from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET

ASSETS = Path("profile/assets")
ASSETS.mkdir(parents=True, exist_ok=True)

FONT = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"

BRAND_DEFS = f"""
  <defs>
    <linearGradient id="darkBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#05070D"/>
      <stop offset="0.55" stop-color="#0A1120"/>
      <stop offset="1" stop-color="#10172A"/>
    </linearGradient>
    <linearGradient id="lightBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/>
      <stop offset="1" stop-color="#EEF2FF"/>
    </linearGradient>
    <linearGradient id="brand" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#37A2FF"/>
      <stop offset="0.5" stop-color="#378ADD"/>
      <stop offset="1" stop-color="#6366F1"/>
    </linearGradient>
    <linearGradient id="brandSoft" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#37A2FF" stop-opacity="0.16"/>
      <stop offset="1" stop-color="#6366F1" stop-opacity="0.16"/>
    </linearGradient>
    <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M36 0H0V36" fill="none" stroke="#94A3B8" stroke-opacity="0.05"/>
    </pattern>
    <filter id="softShadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#000" flood-opacity="0.32"/>
    </filter>
    <filter id="liftShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#0F172A" flood-opacity="0.14"/>
    </filter>
  </defs>
"""


def svg(width: int, height: int, body: str) -> str:
    return (
        f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        f'fill="none" xmlns="http://www.w3.org/2000/svg" font-family="{FONT}">'
        f'{BRAND_DEFS}{body}</svg>'
    )


def cover() -> str:
    body = f"""
  <rect width="1400" height="640" rx="28" fill="url(#darkBg)"/>
  <rect width="1400" height="640" rx="28" fill="url(#grid)"/>
  <circle cx="1120" cy="120" r="320" fill="#37A2FF" fill-opacity="0.18"/>
  <circle cx="1240" cy="540" r="260" fill="#6366F1" fill-opacity="0.18"/>
  <rect x="1.5" y="1.5" width="1397" height="637" rx="26.5" stroke="#37A2FF" stroke-opacity="0.35" stroke-width="2"/>

  <g transform="translate(72 64)">
    <rect width="220" height="38" rx="19" fill="#0F172A" stroke="#22C55E" stroke-opacity="0.45"/>
    <circle cx="22" cy="19" r="6" fill="#22C55E"/>
    <text x="38" y="24" fill="#86EFAC" font-size="13" font-weight="800" letter-spacing="1.2">MAINNET LIVE</text>
    <rect x="234" width="170" height="38" rx="19" fill="#0F172A" stroke="#37A2FF" stroke-opacity="0.45"/>
    <text x="252" y="24" fill="#7DD3FC" font-size="13" font-weight="800" letter-spacing="1.2">E2EE GUARDED</text>
    <rect x="418" width="170" height="38" rx="19" fill="#0F172A" stroke="#A78BFA" stroke-opacity="0.45"/>
    <text x="436" y="24" fill="#DDD6FE" font-size="13" font-weight="800" letter-spacing="1.2">NON-CUSTODIAL</text>
  </g>

  <g transform="translate(72 140)" filter="url(#softShadow)">
    <rect width="116" height="116" rx="30" fill="url(#brand)"/>
    <path d="M36 74C41 80 49 83 59 83C71 83 79 76 79 67C79 57 71 53 60 51L53 50C47 49 44 47 44 43C44 39 49 36 56 36C64 36 70 39 73 44L80 37C75 31 67 28 57 28C45 28 36 35 36 44C36 54 44 58 56 60L62 61C68 62 71 64 71 68C71 72 67 75 60 75C52 75 46 72 41 67L36 74Z" fill="white"/>
    <path d="M30 30H86" stroke="white" stroke-opacity="0.36" stroke-width="5" stroke-linecap="round"/>
    <path d="M30 86H86" stroke="white" stroke-opacity="0.36" stroke-width="5" stroke-linecap="round"/>
  </g>

  <text x="218" y="194" fill="#F8FAFC" font-size="38" font-weight="800" letter-spacing="-0.5">Sudo App</text>
  <text x="218" y="232" fill="#7DD3FC" font-size="17" font-weight="700" letter-spacing="2.4">NON-CUSTODIAL WEB3 MESSENGER</text>

  <text x="72" y="312" fill="#F8FAFC" font-size="64" font-weight="900" letter-spacing="-2">Chat. Pay. Settle.</text>
  <text x="72" y="368" fill="#F8FAFC" font-size="64" font-weight="900" letter-spacing="-2">On-chain. Off-record.</text>

  <text x="72" y="416" fill="#CBD5E1" font-size="20">Connect your wallet to chat, host voice and video meetings,</text>
  <text x="72" y="446" fill="#CBD5E1" font-size="20">send crypto in-line, and settle deals through validator escrow.</text>

  <g transform="translate(72 488)">
    <rect width="142" height="50" rx="25" fill="url(#brand)"/>
    <text x="71" y="32" text-anchor="middle" fill="white" font-size="16" font-weight="800">Open su.do</text>
    <rect x="158" width="172" height="50" rx="25" fill="#0F172A" stroke="#378ADD" stroke-opacity="0.55"/>
    <text x="244" y="32" text-anchor="middle" fill="#BAE6FD" font-size="16" font-weight="800">Get sudochat.app</text>
    <rect x="346" width="216" height="50" rx="25" fill="#0F172A" stroke="#334155"/>
    <text x="454" y="32" text-anchor="middle" fill="#E2E8F0" font-size="16" font-weight="800">Follow @sudomessenger</text>
  </g>

  <g transform="translate(880 110)" filter="url(#softShadow)">
    <rect width="316" height="460" rx="44" fill="#0A0F1C" stroke="#26344D" stroke-width="2"/>
    <rect x="24" y="28" width="268" height="404" rx="34" fill="#0E1626"/>

    <rect x="48" y="64" width="120" height="14" rx="7" fill="#26344D"/>
    <rect x="48" y="86" width="80" height="10" rx="5" fill="#1E293B"/>

    <rect x="48" y="118" width="172" height="58" rx="22" fill="#1E293B"/>
    <text x="68" y="142" fill="#F8FAFC" font-size="13" font-weight="800">GM, wallet connected</text>
    <text x="68" y="160" fill="#94A3B8" font-size="11">0xA4...91d2</text>

    <rect x="84" y="188" width="160" height="56" rx="22" fill="url(#brand)"/>
    <text x="100" y="212" fill="white" font-size="13" font-weight="800">Send 0.25 ETH</text>
    <text x="100" y="230" fill="white" fill-opacity="0.85" font-size="11">to alex.eth</text>

    <rect x="48" y="258" width="220" height="90" rx="20" fill="#0B1220" stroke="#26344D"/>
    <text x="68" y="284" fill="#94A3B8" font-size="11" font-weight="800" letter-spacing="1.4">SUDO WALLET</text>
    <text x="68" y="316" fill="#F8FAFC" font-size="26" font-weight="800">$12,480.50</text>
    <rect x="68" y="324" width="64" height="20" rx="10" fill="#064E3B"/>
    <text x="100" y="338" text-anchor="middle" fill="#A7F3D0" font-size="10" font-weight="800">+8.4%</text>

    <rect x="48" y="362" width="220" height="50" rx="18" fill="#172554" stroke="#1D4ED8"/>
    <circle cx="72" cy="387" r="10" fill="#3B82F6"/>
    <text x="92" y="384" fill="#BFDBFE" font-size="13" font-weight="800">Escrow milestone</text>
    <text x="92" y="402" fill="#93C5FD" font-size="11">2 of 3 validators signed</text>
  </g>

  <g transform="translate(1212 200)" filter="url(#softShadow)">
    <rect width="156" height="92" rx="20" fill="#0F172A" stroke="#26344D"/>
    <text x="20" y="34" fill="#7DD3FC" font-size="11" font-weight="800" letter-spacing="1.4">LIVE CALL</text>
    <text x="20" y="58" fill="#F8FAFC" font-size="18" font-weight="800">4 participants</text>
    <text x="20" y="78" fill="#94A3B8" font-size="11">E2EE - LiveKit</text>
  </g>
  <g transform="translate(1212 312)" filter="url(#softShadow)">
    <rect width="156" height="92" rx="20" fill="#0F172A" stroke="#26344D"/>
    <text x="20" y="34" fill="#A7F3D0" font-size="11" font-weight="800" letter-spacing="1.4">VALIDATORS</text>
    <text x="20" y="58" fill="#F8FAFC" font-size="18" font-weight="800">11 / 11 up</text>
    <text x="20" y="78" fill="#94A3B8" font-size="11">consensus 99.98%</text>
  </g>

  <g transform="translate(72 596)">
    <text x="0" y="0" fill="#475569" font-size="11" font-weight="800" letter-spacing="3">WALLET IDENTITY  -  ENCRYPTED CHAT  -  CRYPTO IN-LINE  -  ESCROW  -  VOICE AND VIDEO  -  SUDO MINING</text>
  </g>
"""
    return svg(1400, 640, body)


def stats() -> str:
    items = [
        ("5", "Repositories", "Org engineering surface", "#37A2FF"),
        ("100%", "Non-custodial", "Keys stay on device", "#6366F1"),
        ("590+", "Wallets supported", "via WalletConnect", "#22C55E"),
        ("11", "Validators", "Mainnet ready", "#F59E0B"),
    ]
    cards = []
    for i, (big, label, sub, color) in enumerate(items):
        x = 64 + i * 322
        cards.append(f"""
  <g transform="translate({x} 56)" filter="url(#liftShadow)">
    <rect width="298" height="148" rx="22" fill="white"/>
    <rect x="0.5" y="0.5" width="297" height="147" rx="21.5" stroke="#E2E8F0"/>
    <rect x="0" y="0" width="6" height="148" rx="3" fill="{color}"/>
    <text x="32" y="68" fill="#0F172A" font-size="44" font-weight="900" letter-spacing="-1.5">{big}</text>
    <text x="32" y="100" fill="#0F172A" font-size="16" font-weight="800">{label}</text>
    <text x="32" y="124" fill="#64748B" font-size="13">{sub}</text>
  </g>
""")
    body = f"""
  <rect width="1400" height="260" rx="22" fill="url(#lightBg)"/>
  <rect x="1" y="1" width="1398" height="258" rx="21" stroke="#DBEAFE" stroke-width="2"/>
  {''.join(cards)}
"""
    return svg(1400, 260, body)


def features() -> str:
    def card(x: int, y: int, w: int, h: int, accent: str, title: str, line1: str, line2: str, tag: str, icon: str) -> str:
        return f"""
  <g transform="translate({x} {y})" filter="url(#softShadow)">
    <rect width="{w}" height="{h}" rx="26" fill="#0F172A" stroke="#1E293B"/>
    <rect x="28" y="28" width="56" height="56" rx="18" fill="{accent}" fill-opacity="0.22"/>
    {icon}
    <text x="28" y="128" fill="#F8FAFC" font-size="24" font-weight="850">{title}</text>
    <text x="28" y="160" fill="#94A3B8" font-size="15">{line1}</text>
    <text x="28" y="182" fill="#94A3B8" font-size="15">{line2}</text>
    <rect x="28" y="{h - 60}" width="160" height="32" rx="16" fill="{accent}" fill-opacity="0.18"/>
    <text x="108" y="{h - 39}" text-anchor="middle" fill="{accent}" font-size="12" font-weight="800" letter-spacing="1.4">{tag}</text>
  </g>
"""

    wallet_icon = (
        '<rect x="42" y="46" width="28" height="22" rx="4" fill="none" stroke="#7DD3FC" stroke-width="2.5"/>'
        '<circle cx="64" cy="57" r="3" fill="#7DD3FC"/>'
    )
    chat_icon = (
        '<path d="M40 48 H72 Q76 48 76 52 V64 Q76 68 72 68 H56 L48 76 V68 H44 Q40 68 40 64 Z" fill="none" stroke="#C4B5FD" stroke-width="2.5" stroke-linejoin="round"/>'
    )
    swap_icon = (
        '<path d="M40 52 H72 L66 46 M76 64 H44 L50 70" fill="none" stroke="#86EFAC" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    escrow_icon = (
        '<path d="M56 42 L72 48 V60 Q72 70 56 76 Q40 70 40 60 V48 Z" fill="none" stroke="#F0ABFC" stroke-width="2.5" stroke-linejoin="round"/>'
        '<path d="M50 58 L55 63 L64 54" fill="none" stroke="#F0ABFC" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    call_icon = (
        '<rect x="40" y="46" width="32" height="22" rx="4" fill="none" stroke="#FDBA74" stroke-width="2.5"/>'
        '<path d="M72 50 L80 46 V68 L72 64 Z" fill="none" stroke="#FDBA74" stroke-width="2.5" stroke-linejoin="round"/>'
    )
    bot_icon = (
        '<rect x="42" y="46" width="28" height="24" rx="6" fill="none" stroke="#FCA5A5" stroke-width="2.5"/>'
        '<circle cx="50" cy="58" r="2.5" fill="#FCA5A5"/>'
        '<circle cx="62" cy="58" r="2.5" fill="#FCA5A5"/>'
        '<path d="M56 42 V46" stroke="#FCA5A5" stroke-width="2.5" stroke-linecap="round"/>'
    )

    body = f"""
  <rect width="1400" height="700" rx="28" fill="url(#darkBg)"/>
  <rect width="1400" height="700" rx="28" fill="url(#grid)"/>
  <rect x="1" y="1" width="1398" height="698" rx="27" stroke="#6366F1" stroke-opacity="0.32" stroke-width="2"/>

  <text x="72" y="86" fill="#7DD3FC" font-size="13" font-weight="900" letter-spacing="3">CAPABILITIES</text>
  <text x="72" y="138" fill="#F8FAFC" font-size="48" font-weight="900" letter-spacing="-1.4">Six surfaces. One conversation.</text>
  <text x="72" y="174" fill="#94A3B8" font-size="18">Sudo unifies wallet, messaging, payments, escrow, meetings and bots inside a single private app.</text>

  {card(72, 220, 410, 222, '#7DD3FC', 'Sudo Wallet', 'Multi-chain custody with seed', 'phrases that never leave device.', 'NON-CUSTODY', wallet_icon)}
  {card(496, 220, 410, 222, '#C4B5FD', 'Encrypted Chat', 'P2P chat, groups, channels,', 'broadcasts and rich media.', 'E2EE', chat_icon)}
  {card(920, 220, 408, 222, '#86EFAC', 'Crypto In-line', 'Send, swap, bridge and open', 'dApps without leaving chat.', 'ON-CHAIN', swap_icon)}
  {card(72, 458, 410, 222, '#F0ABFC', 'Validator Escrow', 'Milestones, dispute resolution,', 'and validator-backed settlement.', 'VALIDATED', escrow_icon)}
  {card(496, 458, 410, 222, '#FDBA74', 'Voice and Video', 'Live meetings, stories, voice', 'notes and screen sharing.', 'LIVEKIT', call_icon)}
  {card(920, 458, 408, 222, '#FCA5A5', 'Web3 Bots', 'Audits, transaction tracking,', 'chain helpers and mini-apps.', 'AUTOMATIONS', bot_icon)}
"""
    return svg(1400, 700, body)


def flow() -> str:
    def phone(x: int, y: int, title: str, inner: str) -> str:
        return f"""
  <g transform="translate({x} {y})" filter="url(#softShadow)">
    <rect width="260" height="380" rx="36" fill="#0A0F1C" stroke="#26344D" stroke-width="2"/>
    <rect x="20" y="22" width="220" height="336" rx="28" fill="#101827"/>
    <text x="40" y="58" fill="#7DD3FC" font-size="11" font-weight="800" letter-spacing="1.5">{title}</text>
    {inner}
  </g>
"""

    chat = (
        '<rect x="40" y="74" width="180" height="50" rx="18" fill="#1E293B"/>'
        '<text x="56" y="98" fill="#F8FAFC" font-size="13" font-weight="700">GM Alex - ready?</text>'
        '<text x="56" y="115" fill="#94A3B8" font-size="11">just now</text>'
        '<rect x="80" y="138" width="140" height="50" rx="18" fill="url(#brand)"/>'
        '<text x="96" y="162" fill="white" font-size="13" font-weight="800">Yes, sending now</text>'
        '<text x="96" y="179" fill="white" fill-opacity="0.85" font-size="11">12:04</text>'
        '<rect x="40" y="208" width="180" height="50" rx="18" fill="#1E293B"/>'
        '<text x="56" y="240" fill="#94A3B8" font-size="12">Typing</text>'
    )
    pay = (
        '<rect x="40" y="74" width="180" height="120" rx="20" fill="#0B1220" stroke="#26344D"/>'
        '<text x="58" y="106" fill="#94A3B8" font-size="11" font-weight="800" letter-spacing="1.4">SEND</text>'
        '<text x="58" y="142" fill="#F8FAFC" font-size="28" font-weight="900">0.25 ETH</text>'
        '<text x="58" y="166" fill="#7DD3FC" font-size="12" font-weight="800">approx $980.40</text>'
        '<rect x="40" y="208" width="180" height="50" rx="18" fill="url(#brand)"/>'
        '<text x="130" y="240" text-anchor="middle" fill="white" font-size="14" font-weight="800">Confirm in wallet</text>'
        '<text x="130" y="296" text-anchor="middle" fill="#475569" font-size="11">gas 0.0006 ETH</text>'
    )
    settle = (
        '<rect x="40" y="74" width="180" height="160" rx="20" fill="#0B1220" stroke="#26344D"/>'
        '<text x="58" y="104" fill="#A7F3D0" font-size="11" font-weight="800" letter-spacing="1.5">SETTLED</text>'
        '<circle cx="76" cy="142" r="12" fill="#064E3B"/>'
        '<path d="M70 142 L75 147 L82 138" stroke="#86EFAC" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
        '<text x="100" y="146" fill="#F8FAFC" font-size="13" font-weight="800">Tx confirmed</text>'
        '<text x="58" y="180" fill="#94A3B8" font-size="11">block 19,402,118</text>'
        '<text x="58" y="200" fill="#94A3B8" font-size="11">3 of 3 validators</text>'
        '<rect x="40" y="252" width="180" height="46" rx="18" fill="#172554" stroke="#1D4ED8"/>'
        '<text x="130" y="280" text-anchor="middle" fill="#BFDBFE" font-size="13" font-weight="800">Share receipt</text>'
    )

    body = f"""
  <rect width="1400" height="560" rx="28" fill="url(#lightBg)"/>
  <rect x="1" y="1" width="1398" height="558" rx="27" stroke="#378ADD" stroke-opacity="0.28" stroke-width="2"/>

  <text x="72" y="80" fill="#378ADD" font-size="13" font-weight="900" letter-spacing="3">THE FLOW</text>
  <text x="72" y="132" fill="#0F172A" font-size="44" font-weight="900" letter-spacing="-1.3">Chat. Pay. Settle.</text>
  <text x="72" y="168" fill="#475569" font-size="18">From a casual message to validator-signed settlement in three taps.</text>

  <g transform="translate(0 30)">
    {phone(120, 180, 'CHAT', chat)}
    {phone(560, 180, 'PAY', pay)}
    {phone(1000, 180, 'SETTLE', settle)}
  </g>

  <g stroke="#94A3B8" stroke-opacity="0.6" stroke-width="2" stroke-dasharray="6 6" fill="none">
    <path d="M408 400 H554"/>
    <path d="M848 400 H994"/>
  </g>
  <g fill="#378ADD">
    <circle cx="554" cy="400" r="5"/>
    <circle cx="994" cy="400" r="5"/>
  </g>
"""
    return svg(1400, 560, body)


def ecosystem() -> str:
    repos = [
        (210, 200, "sudo_app", "Flutter mobile", "#37A2FF"),
        (210, 380, "protocol", "Admin + APIs", "#6366F1"),
        (1190, 200, "website", "Public web", "#22C55E"),
        (1190, 380, "docs", "Specifications", "#F59E0B"),
        (700, 480, "whitepaper", "Research", "#F472B6"),
    ]
    nodes = []
    lines = []
    for cx, cy, name, sub, color in repos:
        lines.append(
            f'<line x1="700" y1="300" x2="{cx}" y2="{cy}" stroke="{color}" stroke-opacity="0.55" stroke-width="2"/>'
        )
        nodes.append(f"""
  <g transform="translate({cx - 130} {cy - 50})" filter="url(#softShadow)">
    <rect width="260" height="100" rx="22" fill="#0F172A" stroke="#1E293B"/>
    <rect x="0" y="0" width="6" height="100" rx="3" fill="{color}"/>
    <text x="28" y="42" fill="#F8FAFC" font-size="20" font-weight="850">{name}</text>
    <text x="28" y="68" fill="#94A3B8" font-size="13">{sub}</text>
    <circle cx="232" cy="50" r="8" fill="{color}" fill-opacity="0.32"/>
    <circle cx="232" cy="50" r="3" fill="{color}"/>
  </g>
""")

    body = f"""
  <rect width="1400" height="640" rx="28" fill="url(#darkBg)"/>
  <rect width="1400" height="640" rx="28" fill="url(#grid)"/>
  <rect x="1" y="1" width="1398" height="638" rx="27" stroke="#37A2FF" stroke-opacity="0.32" stroke-width="2"/>

  <text x="72" y="80" fill="#7DD3FC" font-size="13" font-weight="900" letter-spacing="3">ENGINEERING MAP</text>
  <text x="72" y="132" fill="#F8FAFC" font-size="44" font-weight="900" letter-spacing="-1.3">Repositories orbit the protocol.</text>
  <text x="72" y="168" fill="#94A3B8" font-size="18">Five private codebases working together as one Web3 messenger platform.</text>

  {''.join(lines)}

  <g transform="translate(620 220)" filter="url(#softShadow)">
    <rect width="160" height="160" rx="80" fill="url(#brand)"/>
    <text x="80" y="86" text-anchor="middle" fill="white" font-size="22" font-weight="900">Sudo</text>
    <text x="80" y="110" text-anchor="middle" fill="white" fill-opacity="0.85" font-size="12" font-weight="800" letter-spacing="2">PROTOCOL</text>
  </g>

  {''.join(nodes)}
"""
    return svg(1400, 640, body)


def stack() -> str:
    columns = [
        ("MOBILE", "#37A2FF", ["Flutter", "Dart", "Riverpod", "Reown AppKit"]),
        ("WEB", "#6366F1", ["TypeScript", "Next.js", "React", "Tailwind"]),
        ("BACKEND", "#22C55E", ["Fastify", "PostgreSQL", "Redis", "LiveKit"]),
        ("INFRA", "#F59E0B", ["Cloudflare", "Nginx", "PM2", "DigitalOcean"]),
    ]
    cols = []
    for i, (title, color, items) in enumerate(columns):
        x = 64 + i * 322
        pills = []
        for j, name in enumerate(items):
            pills.append(f"""
    <rect x="0" y="{j * 56}" width="298" height="44" rx="14" fill="white" stroke="#E2E8F0"/>
    <circle cx="22" cy="{j * 56 + 22}" r="5" fill="{color}"/>
    <text x="42" y="{j * 56 + 28}" fill="#0F172A" font-size="15" font-weight="800">{name}</text>
""")
        cols.append(f"""
  <g transform="translate({x} 240)" filter="url(#liftShadow)">
    <text x="0" y="0" fill="{color}" font-size="13" font-weight="900" letter-spacing="3">{title}</text>
    <g transform="translate(0 28)">
      {''.join(pills)}
    </g>
  </g>
""")

    body = f"""
  <rect width="1400" height="520" rx="28" fill="url(#lightBg)"/>
  <rect x="1" y="1" width="1398" height="518" rx="27" stroke="#378ADD" stroke-opacity="0.28" stroke-width="2"/>

  <text x="72" y="80" fill="#378ADD" font-size="13" font-weight="900" letter-spacing="3">STACK</text>
  <text x="72" y="132" fill="#0F172A" font-size="44" font-weight="900" letter-spacing="-1.3">Production grade across the stack.</text>
  <text x="72" y="168" fill="#475569" font-size="18">A focused selection of tools for mobile, web, services and operations.</text>

  {''.join(cols)}
"""
    return svg(1400, 520, body)


def footer() -> str:
    body = f"""
  <rect width="1400" height="320" rx="28" fill="url(#darkBg)"/>
  <circle cx="200" cy="160" r="220" fill="#37A2FF" fill-opacity="0.12"/>
  <circle cx="1200" cy="240" r="240" fill="#6366F1" fill-opacity="0.14"/>
  <rect x="1" y="1" width="1398" height="318" rx="27" stroke="#6366F1" stroke-opacity="0.34" stroke-width="2"/>

  <g transform="translate(72 86)" filter="url(#softShadow)">
    <rect width="116" height="116" rx="30" fill="url(#brand)"/>
    <path d="M36 74C41 80 49 83 59 83C71 83 79 76 79 67C79 57 71 53 60 51L53 50C47 49 44 47 44 43C44 39 49 36 56 36C64 36 70 39 73 44L80 37C75 31 67 28 57 28C45 28 36 35 36 44C36 54 44 58 56 60L62 61C68 62 71 64 71 68C71 72 67 75 60 75C52 75 46 72 41 67L36 74Z" fill="white"/>
    <path d="M30 30H86" stroke="white" stroke-opacity="0.36" stroke-width="5" stroke-linecap="round"/>
    <path d="M30 86H86" stroke="white" stroke-opacity="0.36" stroke-width="5" stroke-linecap="round"/>
  </g>

  <text x="220" y="124" fill="#F8FAFC" font-size="36" font-weight="900" letter-spacing="-1">Build with Sudo.</text>
  <text x="220" y="160" fill="#CBD5E1" font-size="18">Messaging, wallet and on-chain trust in one non-custodial app.</text>

  <g transform="translate(220 196)">
    <rect width="138" height="46" rx="23" fill="url(#brand)"/>
    <text x="69" y="30" text-anchor="middle" fill="white" font-size="15" font-weight="800">su.do</text>
    <rect x="154" width="172" height="46" rx="23" fill="#0F172A" stroke="#378ADD" stroke-opacity="0.55"/>
    <text x="240" y="30" text-anchor="middle" fill="#BAE6FD" font-size="15" font-weight="800">sudochat.app</text>
    <rect x="342" width="216" height="46" rx="23" fill="#0F172A" stroke="#334155"/>
    <text x="450" y="30" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="800">@sudomessenger</text>
    <rect x="574" width="220" height="46" rx="23" fill="#0F172A" stroke="#334155"/>
    <text x="684" y="30" text-anchor="middle" fill="#E2E8F0" font-size="15" font-weight="800">legal@sudochat.app</text>
  </g>

  <text x="72" y="284" fill="#475569" font-size="11" font-weight="800" letter-spacing="2">SUDO GOVERNING COUNCIL  -  SUDO, SUDO CHAT AND THE SUDO LOGO ARE TRADEMARKS OF THE SUDO GOVERNING COUNCIL.</text>
"""
    return svg(1400, 320, body)


def main() -> None:
    pages = {
        "cover.svg": cover(),
        "stats.svg": stats(),
        "features.svg": features(),
        "flow.svg": flow(),
        "ecosystem.svg": ecosystem(),
        "stack.svg": stack(),
        "footer.svg": footer(),
    }
    for name, content in pages.items():
        path = ASSETS / name
        path.write_text(content, encoding="utf-8")
        ET.fromstring(content)
        print(f"OK {path}")


if __name__ == "__main__":
    main()
