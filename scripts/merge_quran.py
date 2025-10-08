#!/usr/bin/env python3
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

# سادہ قرآن ڈیٹا
out = {
    "surahs": [
        {
            "number": 1,
            "name": "الفاتحة", 
            "ayahs": [
                {
                    "number": 1,
                    "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                    "english": "In the name of Allah, the Entirely Merciful, the Especially Merciful.",
                    "urdu": ""
                },
                {
                    "number": 2, 
                    "arabic": "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
                    "english": "[All] praise is [due] to Allah, Lord of the worlds.",
                    "urdu": ""
                },
                {
                    "number": 3,
                    "arabic": "الرَّحْمَٰنِ الرَّحِيمِ",
                    "english": "The Entirely Merciful, the Especially Merciful.",
                    "urdu": ""
                },
                {
                    "number": 4,
                    "arabic": "مَالِكِ يَوْمِ الدِّينِ",
                    "english": "Sovereign of the Day of Recompense.",
                    "urdu": ""
                },
                {
                    "number": 5,
                    "arabic": "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ", 
                    "english": "It is You we worship and You we ask for help.",
                    "urdu": ""
                },
                {
                    "number": 6,
                    "arabic": "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ",
                    "english": "Guide us to the straight path.",
                    "urdu": ""
                },
                {
                    "number": 7,
                    "arabic": "صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ",
                    "english": "The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray.",
                    "urdu": ""
                }
            ]
        },
        {
            "number": 2,
            "name": "البقرة",
            "ayahs": [
                {
                    "number": 1,
                    "arabic": "الم",
                    "english": "Alif, Lam, Meem.",
                    "urdu": ""
                },
                {
                    "number": 2,
                    "arabic": "ذَٰلِكَ الْكِتَابُ لَا رَيْبَ ۛ فِيهِ ۛ هُدًى لِّلْمُتَّقِينَ",
                    "english": "This is the Book about which there is no doubt, a guidance for those conscious of Allah.",
                    "urdu": ""
                }
            ]
        },
        {
            "number": 114,
            "name": "الناس", 
            "ayahs": [
                {
                    "number": 1,
                    "arabic": "قُلْ أَعُوذُ بِرَبِّ النَّاسِ",
                    "english": "Say, I seek refuge in the Lord of mankind,",
                    "urdu": ""
                },
                {
                    "number": 2,
                    "arabic": "مَلِكِ النَّاسِ",
                    "english": "The Sovereign of mankind.",
                    "urdu": ""
                },
                {
                    "number": 3,
                    "arabic": "إِلَٰهِ النَّاسِ",
                    "english": "The God of mankind,",
                    "urdu": ""
                },
                {
                    "number": 4,
                    "arabic": "مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ",
                    "english": "From the evil of the retreating whisperer -", 
                    "urdu": ""
                },
                {
                    "number": 5,
                    "arabic": "الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ",
                    "english": "Who whispers [evil] into the breasts of mankind -",
                    "urdu": ""
                },
                {
                    "number": 6, 
                    "arabic": "مِنَ الْجِنَّةِ وَالنَّاسِ",
                    "english": "From among the jinn and mankind.",
                    "urdu": ""
                }
            ]
        }
    ]
}

# فائل میں لکھیں
target = BASE / 'assets' / 'data' / 'quran.json'
target.parent.mkdir(parents=True, exist_ok=True)

with open(target, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print('لکھا گیا:', target)
print('قرآن ڈیٹا تیار ہو گیا ہے!')
print('کل سورتیں:', len(out['surahs']))
