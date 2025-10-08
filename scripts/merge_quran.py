#!/usr/bin/env python3
# scripts/merge_quran.py
# Quran data merger without external dependencies
import os, json, subprocess, sys
from pathlib import Path
import urllib.request
import time

BASE = Path(__file__).resolve().parent.parent

def download_quran_data():
    """urllib کے ساتھ قرآن ڈیٹا ڈاؤنلوڈ کریں"""
    print("API سے قرآن ڈیٹا ڈاؤنلوڈ ہو رہا ہے...")
    
    try:
        # عربی قرآن ڈیٹا
        print("عربی ڈیٹا ڈاؤنلوڈ ہو رہا ہے...")
        with urllib.request.urlopen('https://api.alquran.cloud/v1/quran/ar.alafasy') as response:
            arabic_data = json.loads(response.read().decode('utf-8'))
        
        time.sleep(1)  # تھوڑا سا انتظار
        
        # انگریزی ترجمہ
        print("انگریزی ترجمہ ڈاؤنلوڈ ہو رہا ہے...")
        with urllib.request.urlopen('https://api.alquran.cloud/v1/quran/en.asad') as response:
            english_data = json.loads(response.read().decode('utf-8'))
        
        return {
            'arabic': arabic_data,
            'english': english_data
        }
    
    except Exception as e:
        print(f"ڈیٹا ڈاؤنلوڈ میں ایرر: {e}")
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

def create_demo_data():
    """اگر ڈاؤنلوڈ نہ ہو سکے تو ڈیمو ڈیٹا بنائیں"""
    print("ڈیمو ڈیٹا تیار کیا جا رہا ہے...")
    
    out = {'surahs': []}
    
    # ڈیمو ڈیٹا - پہلی 2 سورتیں
    demo_surahs = [
        {
            'number': 1, 
            'name': 'الفاتحة', 
            'english_name': 'Al-Fatiha',
            'revelation_type': 'Meccan',
            'ayahs': [
                {
                    'number': 1, 
                    'arabic': 'بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ', 
                    'english': 'In the name of Allah, the Entirely Merciful, the Especially Merciful.', 
                    'urdu': '',
                    'juz': 1,
                    'page': 1
                },
                {
                    'number': 2, 
                    'arabic': 'الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ', 
                    'english': '[All] praise is [due] to Allah, Lord of the worlds.', 
                    'urdu': '',
                    'juz': 1,
                    'page': 1
                }
            ]
        },
        {
            'number': 2, 
            'name': 'البقرة', 
            'english_name': 'Al-Baqarah',
            'revelation_type': 'Medinan',
            'ayahs': [
                {
                    'number': 1, 
                    'arabic': 'الم', 
                    'english': 'Alif, Lam, Meem.', 
                    'urdu': '',
                    'juz': 1,
                    'page': 2
                }
            ]
        }
    ]
    
    out['surahs'] = demo_surahs
    return out

def main():
    print("قرآن ڈیٹا ڈاؤنلوڈ اور مرج کرنا شروع کریں...")
    
    # API سے ڈیٹا ڈاؤنلوڈ کریں
    quran_data = download_quran_data()
    
    if quran_data:
        # ڈیٹا مرج کریں
        print("ڈیٹا مرج ہو رہا ہے...")
        merged_data = merge_quran_data(quran_data)
        print(f"API سے ڈیٹا ڈاؤنلوڈ ہو گیا، کل {len(merged_data['surahs'])} سورتیں")
    else:
        # ڈیمو ڈیٹا بنائیں
        print("API سے ڈیٹا ڈاؤنلوڈ نہیں ہو سکا، ڈیمو ڈیٹا تیار کیا جا رہا ہے...")
        merged_data = create_demo_data()
        print(f"ڈیمو ڈیٹا تیار ہو گیا، کل {len(merged_data['surahs'])} سورتیں")
    
    # فائل میں محفوظ کریں
    target = BASE / 'assets' / 'data' / 'quran.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    
    with open(target, 'w', encoding='utf-8') as f: 
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print('لکھا گیا:', target)
    print('قرآن ڈیٹا تیار ہو گیا ہے!')

if __name__ == "__main__":
    main()
