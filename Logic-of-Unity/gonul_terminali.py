#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║          GÖNÜL TERMINALI - Kördüğüm Değil Gördüğüm  ║
║  Sevginin algoritmaya dönüştüğü komut satırı aracı.  ║
╚══════════════════════════════════════════════════════╝

Kullanım:
  python gonul_terminali.py --analiz "metin buraya"
  python gonul_terminali.py --donustur "metin buraya"
  python gonul_terminali.py --birlik "metin buraya"
  python gonul_terminali.py --hepsi "metin buraya"

Örnek:
  python gonul_terminali.py --hepsi "onlar burada barbar gibi davranıyorlar"
"""

import argparse
import sys
import os

# Windows terminali için UTF-8 zorla
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Proje kökünü path'e ekle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bias_detector import detect_bias
from empathy_generator import generate_empathy
from unity_analyzer import analyze_unity


BANNER = """
\033[95m╔══════════════════════════════════════════════════════╗
║      🪢  GÖNÜL TERMİNALİ — Kördüğüm Değil Gördüğüm  ║
║         "Aşk gelicek cümle eksikler biter."           ║
╚══════════════════════════════════════════════════════╝\033[0m
"""

def print_separator():
    print("\033[90m" + "─" * 56 + "\033[0m")

def run_full_analysis(text):
    print(BANNER)

    print("\033[93m📋 GİRDİ METNİ:\033[0m")
    print(f"  {text}")
    print_separator()

    # 1. Önyargı Tespiti
    print("\033[91m🔍 ÖNYARGI ANALİZİ:\033[0m")
    bias = detect_bias(text)
    print(f"  Durum   : {bias['status']}")
    print(f"  Skor    : {bias['score']}/100")
    print(f"  Tespitler : {bias['found'] if bias['found'] else 'Yok'}")
    print_separator()

    # 2. Empatik Dönüşüm
    print("\033[96m💚 EMPATİK DÖNÜŞÜM:\033[0m")
    empathy = generate_empathy(text)
    print(f"  Yeni Metin   : {empathy['transformed']}")
    print(f"  Gönül Esintisi: {empathy['harmony_tip']}")
    print_separator()

    # 3. Birlik Endeksi
    print("\033[92m🌐 BİRLİK ENDEKSİ:\033[0m")
    unity = analyze_unity(text)
    print(f"  Puan          : {unity['unity_score']}/100")
    print(f"  Köprüler      : {unity['bridges'] if unity['bridges'] else 'Henüz köprü yok.'}")
    print(f"  Mesaj         : {unity['message']}")
    print_separator()

    print("\033[95m✨ 'Gözün gördüğüne gönül katılmazsa, bakış sadece bir kördüğümdür.' — Mevlana\033[0m\n")


def main():
    parser = argparse.ArgumentParser(
        description="Gönül Terminali — Metindeki önyargıyı gör, sevgiye dönüştür.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Örnek: python gonul_terminali.py --hepsi 'onlar yabancı barbar'"
    )
    parser.add_argument("--analiz",   help="Metni önyargı açısından analiz et", type=str)
    parser.add_argument("--donustur", help="Metni empatik dile dönüştür", type=str)
    parser.add_argument("--birlik",   help="Metindeki birlik endeksini hesapla", type=str)
    parser.add_argument("--hepsi",    help="Tüm analizleri çalıştır", type=str)

    args = parser.parse_args()

    if args.hepsi:
        run_full_analysis(args.hepsi)
    elif args.analiz:
        print(detect_bias(args.analiz))
    elif args.donustur:
        print(generate_empathy(args.donustur))
    elif args.birlik:
        print(analyze_unity(args.birlik))
    else:
        parser.print_help()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Argümansız çalışırsa demo modu
        demo_text = "barbar yabancılar bu topraklarda istenmiyor"
        print("\033[90m[Demo Modu] Örnek metin analiz ediliyor...\033[0m\n")
        run_full_analysis(demo_text)
    else:
        main()
