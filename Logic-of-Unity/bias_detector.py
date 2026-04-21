import re

def detect_bias(text):
    """
    Gelişmiş Önyargı ve Nefret Dili Tespit Aracı.
    Çok dilli anahtar kelime desteği ve şiddet skoru hesaplama.
    """
    # Çok dilli önyargı sözlüğü (Genişletilmiş)
    bias_map = {
        "High": [
            r"aşağılık", r"üstün ırk", r"pis \w+", r"barbar", r"defol",
            r"inferior", r"supreme race", r"scum", r"savage", r"get out",
            r"sous-homme", r"race supérieure", r"déshumanisé"
        ],
        "Medium": [
            r"yobaz", r"medeni olmayan", r"gerici", r"tuhaf bunlar",
            r"bigot", r"uncivilized", r"backward", r"those people",
            r"étroit d'esprit", r"non civilisé"
        ],
        "Subtle": [
            r"onlar hep böyle", r"zaten belliydi", r"tipik",
            r"they always", r"it was obvious", r"typical",
            r"ils sont toujours comme ça", r"c'était évident"
        ]
    }
    
    found_biases = []
    severity_score = 0
    
    for level, patterns in bias_map.items():
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                found_biases.extend(matches)
                if level == "High": severity_score += 10 * len(matches)
                elif level == "Medium": severity_score += 5 * len(matches)
                else: severity_score += 2 * len(matches)
                
    return {
        "found": list(set(found_biases)),
        "score": severity_score,
        "status": "DİKKAT" if severity_score > 0 else "TEMİZ"
    }

if __name__ == "__main__":
    test_cases = [
        "Bu barbarlar ve yobazlar buraya ait değil.",
        "They always behave typical like that.",
        "Herkes eşittir ve bir bütündür."
    ]
    
    for test in test_cases:
        result = detect_bias(test)
        print(f"Metin: {test}")
        print(f"Sonuç: {result['status']} (Skor: {result['score']}) - Tespitler: {result['found']}\n")
