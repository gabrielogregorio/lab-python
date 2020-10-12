from fnmatch import fnmatch, fnmatchcase

# Usa as mesmas expressões no Unix
print(fnmatch('arquivo.txt', '*.txt'))
print(fnmatch('arquivo.txt', '*.TXT'))

# Correspondência Exata?
print(fnmatchcase('arquivo.txt', '*.txt'))
print(fnmatchcase('arquivo.txt', '*.TXT'))
# ??? QUAL É A DIFERENÇA? SEI LÁ

print(fnmatch('arquivo.db', '*.txt'))
print(fnmatch('arquivo1.db', 'arquivo[0-9]*'))
print(fnmatch('arquivo1.db', 'arquiv[0-9]*'))


