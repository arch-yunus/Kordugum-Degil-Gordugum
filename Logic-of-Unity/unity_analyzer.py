def analyze_unity(text):
    """
    Metindeki 'Gönül Köprüleri'ni (Birleştirici kelimeleri) tespit eder.
    Birlik ve beraberlik dilinin yoğunluğunu ölçer.
    """
    unity_keywords = {
        "Sevgi/Aşk": [r"sevgi", r"aşk", r"muhabbet", r"love", r"amour", r"haber"],
        "Kardeşlik": [r"kardeş", r"dost", r"yol arkadaşı", r"brother", r"sister", r"fraternité"],
        "Birlik": [r"birlik", r"beraberlik", r"bütün", r"unity", r"unite", r"oneness"],
        "Hoşgörü": [r"hoşgörü", r"sabır", r"anlayış", r"tolerance", r"understanding"],
        "Paylaşım": [r"paylaşmak", r"bölüşmek", r"share", r"partage"]
    }
    
    import re
    bridges_found = {}
    total_matches = 0
    
    for category, patterns in unity_keywords.items():
        matches = []
        for pattern in patterns:
            m = re.findall(pattern, text, re.IGNORECASE)
            if m:
                matches.extend(m)
        if matches:
            bridges_found[category] = len(matches)
            total_matches += len(matches)
            
    unity_index = min(100, (total_matches * 15)) # Basit bir endeks
    
    return {
        "unity_score": unity_index,
        "bridges": bridges_found,
        "message": "Gönül kapıları sonuna kadar açık!" if unity_index > 50 else "Daha fazla köprü kurulabilir."
    }

if __name__ == "__main__":
    texts = [
        "Biz sevgiyle, dostlukla ve birlik içinde bir dünya kuracağız.",
        "Nefret değil, hoşgörü ve paylaşmak bizi kurtaracak.",
        "Sıradan bir gün."
    ]
    
    for t in texts:
        analysis = analyze_unity(t)
        print(f"Metin: {t}")
        print(f"Birlik Endeksi: {analysis['unity_score']}/100")
        print(f"Kurulan Köprüler: {analysis['bridges']}")
        print(f"Durum: {analysis['message']}\n")
