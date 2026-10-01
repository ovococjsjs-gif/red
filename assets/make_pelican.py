#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate assets/pelican_on_bicycle.svg (1000x1000, pure vector, no raster)."""
import math

W = H = 1000
SPOKES = 16


def polar(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def spokes(cx, cy, r, n=SPOKES):
    out = []
    for i in range(n):
        a = 360.0 * i / n
        x1, y1 = polar(cx, cy, r - 12, a)
        x2, y2 = polar(cx, cy, 20, a)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    return "\n      ".join(out)


def wheel(cx, cy, gid):
    return f"""  <g id="{gid}">
    <circle cx="{cx}" cy="{cy}" r="188" fill="none" stroke="url(#tire)" stroke-width="26"/>
    <circle cx="{cx}" cy="{cy}" r="170" fill="none" stroke="url(#rim)" stroke-width="13"/>
    <g stroke="#9aa7b4" stroke-width="4.5" stroke-linecap="round" opacity=".95">
      {spokes(cx, cy, 168)}
    </g>
    <circle cx="{cx}" cy="{cy}" r="24" fill="url(#steel)" stroke="#4b5866" stroke-width="3"/>
    <circle cx="{cx}" cy="{cy}" r="9" fill="#2b3440"/>
    <circle cx="{cx - 7}" cy="{cy - 8}" r="5" fill="#ffffff" opacity=".45"/>
  </g>"""


def tread(cx, cy):
    out = []
    for i in range(28):
        a = 360.0 * i / 28 + 6
        x1, y1 = polar(cx, cy, 197, a)
        x2, y2 = polar(cx, cy, 184, a)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    return f"""  <g stroke="#0d141b" stroke-width="6" stroke-linecap="round" opacity=".35">
      {chr(10).join('      ' + o for o in out)}
    </g>"""


REAR = (310, 690)
FRONT = (740, 690)
BB = (498, 706)
SEAT = (428, 462)
HEAD_TOP = (668, 438)
HEAD_BOT = (700, 546)
PED_NEAR = (570, 758)
PED_FAR = (424, 671)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     role="img" aria-labelledby="ttl desc">
  <title id="ttl">Pelican riding a bicycle</title>
  <desc id="desc">A white pelican with an orange beak and a pink throat pouch rides a blue
  bicycle along a sunny road: wings on the handlebars, webbed feet on the pedals.</desc>

  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#cfeaf8"/>
      <stop offset=".55" stop-color="#eaf6fc"/>
      <stop offset="1" stop-color="#fdf6e9"/>
    </linearGradient>
    <radialGradient id="sun" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="#fff3c4" stop-opacity=".95"/>
      <stop offset="1" stop-color="#fff3c4" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="road" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e6d9c3"/>
      <stop offset="1" stop-color="#cbbb9e"/>
    </linearGradient>
    <linearGradient id="tire" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3c4753"/>
      <stop offset="1" stop-color="#1d252e"/>
    </linearGradient>
    <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e4eaf0"/>
      <stop offset=".5" stop-color="#b6c2cf"/>
      <stop offset="1" stop-color="#8d9aa8"/>
    </linearGradient>
    <radialGradient id="steel" cx=".35" cy=".35" r=".8">
      <stop offset="0" stop-color="#f2f5f8"/>
      <stop offset=".55" stop-color="#b9c4cf"/>
      <stop offset="1" stop-color="#78848f"/>
    </radialGradient>
    <linearGradient id="body" x1=".2" y1="0" x2=".75" y2="1">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset=".45" stop-color="#f8fbfd"/>
      <stop offset="1" stop-color="#d5e0ea"/>
    </linearGradient>
    <linearGradient id="wing" x1="0" y1="0" x2=".8" y2="1">
      <stop offset="0" stop-color="#f4f8fb"/>
      <stop offset=".6" stop-color="#dfe8f0"/>
      <stop offset="1" stop-color="#bcc9d6"/>
    </linearGradient>
    <linearGradient id="beak" x1="0" y1="0" x2="1" y2=".6">
      <stop offset="0" stop-color="#ffc247"/>
      <stop offset=".55" stop-color="#ffa02c"/>
      <stop offset="1" stop-color="#ef7d16"/>
    </linearGradient>
    <linearGradient id="pouch" x1=".2" y1="0" x2=".6" y2="1">
      <stop offset="0" stop-color="#ffc9a6"/>
      <stop offset=".45" stop-color="#fca877"/>
      <stop offset="1" stop-color="#e9744f"/>
    </linearGradient>
    <linearGradient id="leg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ffc247"/>
      <stop offset="1" stop-color="#f08c1c"/>
    </linearGradient>
    <radialGradient id="shadow" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="#6b5b45" stop-opacity=".45"/>
      <stop offset="1" stop-color="#6b5b45" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="cheek" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="#f9a27c" stop-opacity=".5"/>
      <stop offset="1" stop-color="#f9a27c" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- ================= background ================= -->
  <rect width="{W}" height="{H}" fill="url(#sky)"/>
  <circle cx="150" cy="140" r="180" fill="url(#sun)"/>
  <g fill="#ffffff" opacity=".8">
    <ellipse cx="255" cy="128" rx="92" ry="36"/>
    <ellipse cx="330" cy="112" rx="66" ry="30"/>
    <ellipse cx="185" cy="114" rx="52" ry="26"/>
    <ellipse cx="880" cy="150" rx="72" ry="26" opacity=".75"/>
    <ellipse cx="822" cy="138" rx="46" ry="20" opacity=".75"/>
  </g>

  <!-- road -->
  <path d="M0 884 H1000 V1000 H0 Z" fill="url(#road)"/>
  <path d="M0 884 H1000" stroke="#a8987c" stroke-width="4" opacity=".7"/>
  <g stroke="#f6f1e4" stroke-width="12" stroke-linecap="round" opacity=".8">
    <line x1="40" y1="952" x2="180" y2="952"/>
    <line x1="260" y1="952" x2="400" y2="952"/>
    <line x1="480" y1="952" x2="620" y2="952"/>
    <line x1="700" y1="952" x2="840" y2="952"/>
    <line x1="920" y1="952" x2="1000" y2="952"/>
  </g>
  <ellipse cx="520" cy="892" rx="400" ry="32" fill="url(#shadow)"/>
  <g fill="#ffffff" opacity=".5">
    <circle cx="205" cy="874" r="13"/><circle cx="172" cy="862" r="8"/><circle cx="238" cy="864" r="7"/>
  </g>
  <!-- motion lines -->
  <g stroke="#9fb3c2" stroke-width="10" stroke-linecap="round" opacity=".5">
    <line x1="52" y1="600" x2="196" y2="600"/>
    <line x1="20" y1="668" x2="140" y2="668"/>
    <line x1="70" y1="736" x2="200" y2="736"/>
  </g>

{wheel(*REAR, 'rear-wheel')}
{tread(*REAR)}

  <!-- ================= far side (behind the frame) ================= -->
  <g id="far-leg">
    <path d="M405 425 L350 540" fill="none" stroke="#c3cfdb" stroke-width="40" stroke-linecap="round"/>
    <path d="M350 540 L{PED_FAR[0]} {PED_FAR[1]}" fill="none" stroke="#d98f22" stroke-width="19" stroke-linecap="round"/>
    <circle cx="350" cy="540" r="18" fill="#cdd8e3"/>
    <g transform="translate({PED_FAR[0]} {PED_FAR[1]}) rotate(12)">
      <path d="M-28 -10 L60 -14 L70 7 L56 18 L-24 17 Z" fill="#e0901f"/>
      <path d="M6 -13 L8 18 M32 -14 L34 17" stroke="#c4761a" stroke-width="4" opacity=".7"/>
    </g>
  </g>
  <line x1="{BB[0]}" y1="{BB[1]}" x2="{PED_FAR[0]}" y2="{PED_FAR[1]}" stroke="#2b3440" stroke-width="16" stroke-linecap="round"/>
  <g transform="translate({PED_FAR[0]} {PED_FAR[1]}) rotate(-6)">
    <rect x="-34" y="-13" width="74" height="26" rx="11" fill="#2b3440"/>
    <rect x="-30" y="-9" width="66" height="7" rx="3.5" fill="#4d5a68"/>
  </g>
  <!-- far wing-arm to the handlebar (behind the bar) -->
  <path d="M600 318 C636 342 664 372 690 392 C704 403 716 408 726 406
           C736 403 737 393 728 389 C714 383 700 382 688 372
           C664 352 640 328 618 306 Z"
        fill="#c6d2de" stroke="#a9b8c7" stroke-width="2"/>

{wheel(*FRONT, 'front-wheel')}
{tread(*FRONT)}

  <!-- ================= frame ================= -->
  <g id="frame" stroke-linecap="round" fill="none">
    <line x1="{REAR[0]}" y1="{REAR[1]}" x2="{BB[0]}" y2="{BB[1]}" stroke="#2a80b2" stroke-width="16"/>
    <line x1="{REAR[0]}" y1="{REAR[1]}" x2="{SEAT[0]}" y2="{SEAT[1]}" stroke="#2a80b2" stroke-width="14"/>
    <line x1="{BB[0]}" y1="{BB[1]}" x2="{SEAT[0]}" y2="{SEAT[1] - 4}" stroke="#2a80b2" stroke-width="21"/>
    <line x1="{BB[0]}" y1="{BB[1]}" x2="{HEAD_BOT[0]}" y2="{HEAD_BOT[1]}" stroke="#2a80b2" stroke-width="23"/>
    <line x1="{SEAT[0]}" y1="{SEAT[1]}" x2="{HEAD_TOP[0]}" y2="{HEAD_TOP[1] + 4}" stroke="#2a80b2" stroke-width="18"/>
    <g stroke="#7cc4e4" stroke-width="5" opacity=".8">
      <line x1="{BB[0] - 5}" y1="{BB[1] - 14}" x2="{SEAT[0] - 3}" y2="{SEAT[1] + 26}"/>
      <line x1="{BB[0] + 14}" y1="{BB[1] - 12}" x2="{HEAD_BOT[0] - 16}" y2="{HEAD_BOT[1] - 10}"/>
      <line x1="{SEAT[0] + 16}" y1="{SEAT[1] - 7}" x2="{HEAD_TOP[0] - 16}" y2="{HEAD_TOP[1] + 5}"/>
      <line x1="{REAR[0] + 16}" y1="{REAR[1] - 6}" x2="{BB[0] - 18}" y2="{BB[1] - 7}"/>
    </g>
    <!-- head tube + fork -->
    <path d="M{HEAD_TOP[0]} {HEAD_TOP[1]} L{HEAD_BOT[0]} {HEAD_BOT[1]}" stroke="#1d5f88" stroke-width="27"/>
    <path d="M{HEAD_BOT[0] - 2} {HEAD_BOT[1]} C{HEAD_BOT[0] + 8} 610 {FRONT[0] - 8} 640 {FRONT[0]} {FRONT[1]}"
          stroke="url(#steel)" stroke-width="16"/>
    <path d="M{HEAD_BOT[0] + 5} {HEAD_BOT[1] + 8} C{HEAD_BOT[0] + 15} 612 {FRONT[0] - 3} 644 {FRONT[0] - 2} {FRONT[1] - 22}"
          stroke="#ffffff" stroke-width="4" opacity=".4"/>
    <!-- stem + handlebar -->
    <path d="M{HEAD_TOP[0] + 2} {HEAD_TOP[1] + 4} L660 386" stroke="#39424d" stroke-width="20"/>
    <path d="M660 386 C692 372 724 380 742 402 C754 416 756 428 752 438"
          stroke="#39424d" stroke-width="18"/>
    <path d="M738 398 C750 412 753 426 750 436" stroke="#1c232b" stroke-width="24" stroke-linecap="round"/>
    <path d="M666 382 C688 374 710 378 726 390" stroke="#6d7a88" stroke-width="5" opacity=".8"/>
    <!-- seatpost + saddle -->
    <path d="M{SEAT[0] + 2} {SEAT[1] + 12} L418 442" stroke="#39424d" stroke-width="18"/>
    <path d="M344 442 C346 424 372 414 404 414 C438 414 462 424 466 438
             C468 448 452 454 424 456 L372 458 C352 458 343 452 344 442 Z"
          fill="#2b3440" stroke="#1a2129" stroke-width="3"/>
    <path d="M360 430 C382 422 424 422 452 432" stroke="#5b6875" stroke-width="5" fill="none" opacity=".8"/>
  </g>

  <!-- ================= drivetrain ================= -->
  <g id="drivetrain">
    <circle cx="{REAR[0]}" cy="{REAR[1]}" r="34" fill="url(#steel)" stroke="#4b5866" stroke-width="4"/>
    <circle cx="{REAR[0]}" cy="{REAR[1]}" r="44" fill="none" stroke="#6b7885" stroke-width="9" stroke-dasharray="5 9"/>
    <path d="M{BB[0] - 4} {BB[1] - 62} L{REAR[0] - 2} {REAR[1] - 42}" stroke="#3b4653" stroke-width="9"/>
    <path d="M{BB[0] - 4} {BB[1] + 62} L{REAR[0] - 2} {REAR[1] + 42}" stroke="#3b4653" stroke-width="9"/>
    <path d="M{BB[0] - 4} {BB[1] - 62} L{REAR[0] - 2} {REAR[1] - 42}" stroke="#93a1ae" stroke-width="4" stroke-dasharray="7 7"/>
    <path d="M{BB[0] - 4} {BB[1] + 62} L{REAR[0] - 2} {REAR[1] + 42}" stroke="#93a1ae" stroke-width="4" stroke-dasharray="7 7"/>
    <circle cx="{BB[0]}" cy="{BB[1]}" r="62" fill="none" stroke="#8b97a4" stroke-width="13" stroke-dasharray="7 11"/>
    <circle cx="{BB[0]}" cy="{BB[1]}" r="52" fill="url(#steel)" stroke="#5d6a77" stroke-width="4"/>
    <g stroke="#5d6a77" stroke-width="11" stroke-linecap="round">
      <line x1="{BB[0] - 24}" y1="{BB[1] - 24}" x2="{BB[0] + 24}" y2="{BB[1] + 24}"/>
      <line x1="{BB[0] + 24}" y1="{BB[1] - 24}" x2="{BB[0] - 24}" y2="{BB[1] + 24}"/>
      <line x1="{BB[0] - 34}" y1="{BB[1] + 4}" x2="{BB[0] + 34}" y2="{BB[1] - 4}"/>
    </g>
    <circle cx="{BB[0]}" cy="{BB[1]}" r="15" fill="#39424d"/>
    <circle cx="{BB[0] - 4}" cy="{BB[1] - 5}" r="5" fill="#93a1ae" opacity=".8"/>
    <!-- near crank + pedal -->
    <line x1="{BB[0]}" y1="{BB[1]}" x2="{PED_NEAR[0]}" y2="{PED_NEAR[1]}" stroke="#39424d" stroke-width="18" stroke-linecap="round"/>
    <line x1="{BB[0] + 6}" y1="{BB[1] + 6}" x2="{PED_NEAR[0] - 4}" y2="{PED_NEAR[1] - 4}" stroke="#6d7a88" stroke-width="5" opacity=".7"/>
    <g transform="translate({PED_NEAR[0]} {PED_NEAR[1]}) rotate(8)">
      <rect x="-38" y="-14" width="82" height="28" rx="12" fill="#39424d"/>
      <rect x="-33" y="-10" width="72" height="8" rx="4" fill="#66737f"/>
    </g>
  </g>

  <!-- ================= pelican ================= -->
  <g id="pelican">
    <!-- tail feathers -->
    <g stroke-linejoin="round">
      <path d="M262 372 C220 362 186 342 164 314 C186 356 216 386 258 402 Z" fill="#dfe8f0" stroke="#c3d0dc" stroke-width="2"/>
      <path d="M258 392 C214 388 178 372 152 348 C178 388 212 412 254 420 Z" fill="#cfd9e3" stroke="#b8c6d4" stroke-width="2"/>
      <path d="M262 412 C226 414 196 404 172 386 C196 416 226 430 262 432 Z" fill="#e9f0f6" stroke="#c3d0dc" stroke-width="2"/>
    </g>

    <!-- near leg -->
    <g id="near-leg">
      <path d="M455 420 L515 545" fill="none" stroke="#e8eff5" stroke-width="48" stroke-linecap="round"/>
      <circle cx="515" cy="545" r="22" fill="#f2f6f9" stroke="#cfd9e3" stroke-width="2"/>
      <path d="M515 545 L566 742" fill="none" stroke="url(#leg)" stroke-width="23" stroke-linecap="round"/>
      <path d="M511 553 L560 736" fill="none" stroke="#ffffff" stroke-width="5" opacity=".35"/>
      <g transform="translate(568 748) rotate(8)">
        <path d="M-34 -12 L66 -16 L80 6 L64 20 L-30 20 Z" fill="url(#leg)" stroke="#d9831c" stroke-width="2"/>
        <path d="M4 -15 L6 20 M32 -16 L34 20" stroke="#dd8a1e" stroke-width="4" opacity=".65"/>
      </g>
    </g>

    <!-- body + neck + head: one silhouette -->
    <path d="M612 352
             C630 306 634 268 644 238
             C668 198 696 202 704 216
             C708 180 678 150 644 150
             C608 150 582 176 582 210
             C584 236 592 254 600 268
             C576 286 550 292 516 292
             C430 286 330 306 262 352
             C226 378 222 412 268 428
             C330 440 420 442 472 436
             C540 428 600 398 612 352 Z"
          fill="url(#body)" stroke="#c3d0dc" stroke-width="3"/>
    <!-- soft shading + highlights on the silhouette -->
    <path d="M600 372 C560 412 500 430 440 432 C380 434 320 428 282 414
             C320 436 380 444 440 442 C510 440 570 416 600 372 Z"
          fill="#c8d4e0" opacity=".55"/>
    <path d="M612 340 C624 300 630 268 638 242" fill="none" stroke="#ffffff" stroke-width="10" opacity=".6" stroke-linecap="round"/>
    <path d="M560 296 C480 292 380 312 300 356" fill="none" stroke="#ffffff" stroke-width="12" opacity=".65" stroke-linecap="round"/>
    <path d="M596 268 C588 252 584 236 584 214" fill="none" stroke="#c8d4e0" stroke-width="6" opacity=".5" stroke-linecap="round"/>

    <!-- wing with pointed feathers -->
    <path d="M505 312
             C562 310 594 340 590 372
             C586 402 548 420 498 426
             C458 430 420 428 388 420
             L268 402 L320 396
             L246 372 L318 372
             L262 340 L330 350
             C360 330 430 316 505 312 Z"
          fill="url(#wing)" stroke="#a9b8c7" stroke-width="2.5" stroke-linejoin="round"/>
    <g fill="none" stroke="#9fb0c0" stroke-width="5" stroke-linecap="round" opacity=".8">
      <path d="M340 396 C392 416 448 422 500 414"/>
      <path d="M352 372 C402 392 452 398 500 392"/>
      <path d="M372 348 C416 364 458 370 500 366"/>
    </g>
    <path d="M470 318 C524 316 566 336 580 364" fill="none" stroke="#ffffff" stroke-width="8" opacity=".6"/>

    <!-- crest -->
    <g fill="#eef4f9" stroke="#c3d0dc" stroke-width="2" stroke-linejoin="round">
      <path d="M586 172 C572 158 564 142 564 126 C576 140 586 154 594 166 Z"/>
      <path d="M600 158 C592 140 590 124 594 110 C602 126 606 142 610 154 Z"/>
    </g>

    <!-- cheek + eye -->
    <circle cx="606" cy="226" r="24" fill="url(#cheek)"/>
    <circle cx="664" cy="194" r="17" fill="#ffd77a" stroke="#e0a53a" stroke-width="3"/>
    <circle cx="666" cy="194" r="10" fill="#231c17"/>
    <circle cx="662" cy="190" r="4" fill="#ffffff"/>
    <path d="M646 176 C656 170 676 170 686 178" fill="none" stroke="#c3d0dc" stroke-width="4"/>

    <!-- beak + pouch -->
    <path d="M696 212 C746 230 806 244 862 242 C878 250 872 268 850 276
             C800 292 742 278 706 246 C698 236 694 224 696 212 Z"
          fill="url(#pouch)" stroke="#dc7a54" stroke-width="2.5"/>
    <path d="M724 244 C770 260 816 266 848 260" fill="none" stroke="#ffffff" stroke-width="6" opacity=".3"/>
    <path d="M690 178 C750 172 822 190 874 220 C888 228 886 242 868 244
             C814 248 746 232 696 212 Z"
          fill="url(#beak)" stroke="#dd871c" stroke-width="2.5"/>
    <path d="M702 188 C754 184 814 200 858 224" fill="none" stroke="#fff0c2" stroke-width="6" opacity=".75"/>
    <path d="M718 194 L742 200" stroke="#d9831c" stroke-width="4" stroke-linecap="round" opacity=".8"/>
    <path d="M696 212 C746 230 806 244 864 242" fill="none" stroke="#c9694a" stroke-width="4" opacity=".7"/>

    <!-- near wing-arm on the handlebar -->
    <path d="M596 330 C634 352 664 384 690 406 C706 420 722 426 736 422
             C748 418 750 406 740 402 C726 396 710 396 696 386
             C672 368 644 340 620 316 Z"
          fill="#eef4f9" stroke="#b8c6d4" stroke-width="2.5"/>
    <path d="M608 330 C638 352 662 378 684 398" fill="none" stroke="#ffffff" stroke-width="6" opacity=".6"/>
    <g transform="translate(742 414) rotate(-18)">
      <ellipse cx="0" cy="0" rx="17" ry="12" fill="#f7fafc" stroke="#c3d0dc" stroke-width="2"/>
      <path d="M-6 -10 L-4 10 M4 -11 L6 10" stroke="#c3d0dc" stroke-width="2.5"/>
    </g>

    <!-- bell -->
    <g>
      <line x1="706" y1="374" x2="706" y2="366" stroke="#39424d" stroke-width="6"/>
      <circle cx="706" cy="360" r="12" fill="#f4c542" stroke="#c9992e" stroke-width="2.5"/>
      <circle cx="702" cy="356" r="4" fill="#fff6d8"/>
      <circle cx="706" cy="371" r="3" fill="#8a6a1e"/>
    </g>
  </g>

  <!-- foreground grass tufts -->
  <g stroke="#9bb08a" stroke-width="6" stroke-linecap="round" opacity=".8" fill="none">
    <path d="M96 884 C92 862 96 848 104 838"/>
    <path d="M110 884 C112 866 120 852 132 846"/>
    <path d="M884 884 C880 864 884 850 894 842"/>
    <path d="M900 884 C904 868 912 856 924 850"/>
  </g>
</svg>
"""

with open("pelican_on_bicycle.svg", "w", encoding="utf-8") as fh:
    fh.write(svg)
print("written", len(svg.encode()), "bytes")
