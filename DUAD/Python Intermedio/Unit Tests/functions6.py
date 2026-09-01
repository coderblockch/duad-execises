def sort_words(text):
    words = text.split("-")      # 1. convertir a lista (separar por guion)
    words.sort()                  # 2. ordenar alfabéticamente
    return "-".join(words)        # 3. convertir de nuevo a string (unir con guion)


# Prueba
print(sort_words("python-variable-funcion-computadora-monitor"))