def converter_notas(nota):
    if nota == '3':
        mencao = 'Very Evident'
    elif nota == '2':
        mencao = 'Evident'
    elif nota == '1':
        mencao = 'Fairly Evident'
    elif nota == '0':
        mencao = 'Not Evident'
    elif nota == '':
        mencao = 'Não aplicável'
    else:
        mencao = nota
    return mencao
