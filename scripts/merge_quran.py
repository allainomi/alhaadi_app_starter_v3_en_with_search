#!/usr/bin/env python3
# scripts/merge_quran.py
# Downloads Quran data and merges Arabic+English translation into assets/data/quran.json
import os, json, subprocess, sys
from pathlib import Path
import requests

BASE = Path(__file__).resolve().parent.parent
SRC_DIR = BASE / 'sources'
SRC_DIR.mkdir(exist_ok=True)

def download_from_api():
    """API سے قرآن ڈیٹا ڈاؤنلوڈ کریں"""
    print("API سے قرآن ڈیٹا ڈاؤنلوڈ ہو رہا ہے...")
    
    try:
        # عربی قرآن ڈیٹا
        print("عربی ڈیٹا ڈاؤنلوڈ ہو رہا ہے...")
        arabic_response = requests.get('https://api.alquran.cloud/v1/quran/ar.alafasy')
        if arabic_response.status_code != 200:
            print("عربی ڈیٹا ڈاؤنلوڈ نہیں ہو سکا")
            return None
        
        # انگریزی ترجمہ
        print("انگریزی ترجمہ ڈاؤنلوڈ ہو رہا ہے...")
        english_response = requests.get('https://api.alquran.cloud/v1/quran/en.asad')
        if english_response.status_code != 200:
            print("انگریزی ترجمہ ڈاؤنلوڈ نہیں ہو سکا")
            return None
        
        return {
            'arabic': arabic_response.json(),
            'english': english_response.json()
        }
    
    except Exception as e:
        print(f"API سے ڈیٹا ڈاؤنلوڈ میں ایرر: {e}")
        return None

def merge_quran_data(quran_data):
    """قرآن ڈیٹا کو مرج کریں"""
    arabic_data = quran_data['arabic']
    english_data = quran_data['english']
    
    out = {'surahs': []}
    
    # ڈیٹا کی ساخت چیک کریں اور مرج کریں
    arabic_surahs = arabic_data['data']['surahs']
    english_surahs = english_data['data']['surahs']
    
    for surah_idx, (arabic_surah, english_surah) in enumerate(zip(arabic_surahs, english_surahs)):
        surah_number = arabic_surah['number']
        surah_name = arabic_surah['name']
        surah_english_name = arabic_surah['englishName']
        revelation_type = arabic_surah['revelationType']
        
        ayahs = []
        for ayah_idx, (arabic_ayah, english_ayah) in enumerate(zip(arabic_surah['ayahs'], english_surah['ayahs'])):
            ayah_data = {
                'number': arabic_ayah['numberInSurah'],
                'arabic': arabic_ayah['text'],
                'english': english_ayah['text'],
                'urdu': '',
                'juz': arabic_ayah.get('juz', 0),
                'page': arabic_ayah.get('page', 0)
            }
            ayahs.append(ayah_data)
        
        surah_data = {
            'number': surah_number,
            'name': surah_name,
            'english_name': surah_english_name,
            'revelation_type': revelation_type,
            'ayahs': ayahs
        }
        out['surahs'].append(surah_data)
    
    return out

def main():
    print("قرآن ڈیٹا ڈاؤنلوڈ اور مرج کرنا شروع کریں...")
    
    # API سے ڈیٹا ڈاؤنلوڈ کریں
    quran_data = download_from_api()
    
    if not quran_data:
        print("ڈیٹا ڈاؤنلوڈ نہیں ہو سکا")
        sys.exit(1)
    
    # ڈیٹا مرج کریں
    print("ڈیٹا مرج ہو رہا ہے...")
    merged_data = merge_quran_data(quran_data)
    
    # فائل میں محفوظ کریں
    target = BASE / 'assets' / 'data' / 'quran.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    
    with open(target, 'w', encoding='utf-8') as f: 
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print('لکھا گیا:', target)
    print(f"کل {len(merged_data['surahs'])} سورتیں مرج ہوئیں")

if __name__ == "__main__":
    main()
