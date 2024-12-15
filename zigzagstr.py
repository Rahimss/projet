import streamlit as st

def zigzag(text, k):
    if k == 1:
        return text

    # nehi l'espace
    positions = [i for i, char in enumerate(text) if char == ' ']
    text = text.replace(' ', '')

    zigzag = [[] for i in range(k)]
    niv = 0
    direction = 1  # 1 for up, -1 for down

    for char in text:
        zigzag[niv].append(char)
        if niv == 0:
            direction = 1
        elif niv == k - 1:
            direction = -1
        niv += direction

    result = ''.join(''.join(line) for line in zigzag)

    # N3awdou nzidou les espaces
    for pos in positions:
        result = result[:pos] + ' ' + result[pos:]

    return result

def dechiffre_zigzag(chiffre_text, k):
    if k == 1:
        return chiffre_text

    # nehi lespace
    positions = [i for i, char in enumerate(chiffre_text) if char == ' ']
    chiffre_text = chiffre_text.replace(' ', '')

    # nahasbou la longueur de chaque niveau
    n = len(chiffre_text)
    zigzag = [[] for i in range(k)]
    niv_lengths = [0] * k
    niv = 0
    direction = 1

    for i in range(n):
        niv_lengths[niv] += 1
        if niv == 0:
            direction = 1
        elif niv == k - 1:
            direction = -1
        niv += direction

    # n3awdou ndirou zigzag Le9dime ta3 chiffrement
    index = 0
    for i in range(k):
        zigzag[i] = list(chiffre_text[index:index + niv_lengths[i]])
        index += niv_lengths[i]

    # dechiffrement ta3 zigzag
    dechiffre_text = []
    niv = 0
    direction = 1
    niv_indices = [0] * k

    for i in range(n):
        dechiffre_text.append(zigzag[niv][niv_indices[niv]])
        niv_indices[niv] += 1
        if niv == 0:
            direction = 1
        elif niv == k - 1:
            direction = -1
        niv += direction

    result = ''.join(dechiffre_text)

    # nrej3ou nzidou les espaces
    for pos in positions:
        result = result[:pos] + ' ' + result[pos:]

    return result

st.title("Zigzag by DEBIECHE")

# User input
user_text = st.text_input("Entrer le texte Sans caractères spéciaux(.,/\....):")
uploaded_file = st.file_uploader("Ou telecharger un fichier texte(Sans caractères spéciaux):", type="txt")
if uploaded_file is not None:
    user_text = uploaded_file.read().decode("utf-8").replace('\n', ' ')

user_k = st.number_input("donner (k) le nombre des niveaux:", min_value=1, value=10)
option = st.selectbox("Choisir:", ("chiffrer", "dechiffrer"))

if st.button("Submit"):
    if option == "chiffrer":
        result = zigzag(user_text, user_k)
    else:
        result = dechiffre_zigzag(user_text, user_k)
    st.write("Resultat:", result)
