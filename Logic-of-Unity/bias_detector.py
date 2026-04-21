import re

def detect_bias(text):
    """
    Basit bir önyargı ve nefret dili tespit algoritması taslağı.
    Gerçek bir uygulamada bu, NLP modelleri (BERT, RoBERTa vb.) ile desteklenmelidir.
    """
    # Örnek ayrımcı veya önyargılı kelime listesi (Basit bir örnek)
    biased_keywords = [
        r"aşağılık", r"üstün ırk", r"pis \w+", r"defol", r"istenmeyen",
        r"barbar", r"yobaz", r"medeni olmayan"
    ]
    
    found_biases = []
    for pattern in biased_keywords:
        if re.search(pattern, text, re.IGNORECASE):
            found_biases.append(pattern)
            
    return found_biases

if __name__ == "__main__":
    sample_text = "Bu barbarlar buraya ait değil."
    biases = detect_bias(sample_text)
    
    if biases:
        print(f"Uyarı: Metinde potansiyel önyargı tespit edildi: {biases}")
    else:
        print("Metin temiz görünüyor (Basit kontrol).")
