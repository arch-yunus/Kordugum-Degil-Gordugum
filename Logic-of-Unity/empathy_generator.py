def generate_empathy(text):
    """
    Sert veya ötekileştirici dili, kapsayıcı ve empatik bir dile çevirme denemesi.
    """
    replacements = {
        "onlar": "kardeşlerimiz",
        "barbar": "kültürel farklılıkları olan değerler",
        "yabancı": "misafir/yeni komşu",
        "nefret ediyorum": "henüz anlamakta zorlanıyorum",
        "defolun": "birlikte yaşamayı öğrenmeliyiz"
    }
    
    words = text.lower().split()
    transformed_text = []
    
    for word in words:
        transformed_word = replacements.get(word, word)
        transformed_text.append(transformed_word)
        
    return " ".join(transformed_text).capitalize()

if __name__ == "__main__":
    toxic_input = "Biz onlardan nefret ediyorum"
    empathetic_output = generate_empathy(toxic_input)
    
    print(f"Orijinal: {toxic_input}")
    print(f"Empatik Dönüşüm: {empathetic_output}")
