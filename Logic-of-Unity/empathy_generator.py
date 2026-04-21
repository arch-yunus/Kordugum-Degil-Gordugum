import re

def generate_empathy(text):
    """
    Sert dili empatik ve birleştirici bir dile dönüştüren araç.
    Eklerin (suffix) korunması için basit regex eşleşmeleri kullanır.
    """
    # Dönüşüm haritası (Kök bazlı)
    transformations = {
        r"\bonlar(ı|a|da|dan|la)?\b": r"kardeşlerimiz\1",
        r"\bbarbar(lar|ın|a|ı)?\b": r"kültür elçileri\1",
        r"\byabancı(lar|ın|a|ı)?\b": r"misafir\1",
        r"\bnefret ediyorum\b": "henüz anlamakta zorlanıyorum",
        r"\bdefol(un)?\b": "birlikte yaşamayı öğrenmeliyiz"
    }
    
    result = text.lower()
    for pattern, replacement in transformations.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
    # Uyum Önerisi (Harmony Suggestion)
    suggestions = [
        "Farklılıklar bizi zayıflatmaz, derinleştirir.",
        "Onun yerinde senin olduğunu hayal etmeyi dene.",
        "Sevgi, her türlü karanlığı dağıtan tek ışıktır."
    ]
    
    import random
    return {
        "transformed": result.capitalize(),
        "harmony_tip": random.choice(suggestions)
    }

if __name__ == "__main__":
    toxic_inputs = [
        "Biz onlardan nefret ediyorum.",
        "Barbarlar buraya gelmemeli.",
        "Yabancıları istemiyoruz."
    ]
    
    for inp in toxic_inputs:
        res = generate_empathy(inp)
        print(f"Orijinal: {inp}")
        print(f"Empatik: {res['transformed']}")
        print(f"Gönül Esintisi: {res['harmony_tip']}\n")
