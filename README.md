# Vigenere
Programa para criptografia usando o método de Vigenère.

> A cifra de Vigenère é um método de criptografia que usa uma série de diferentes cifras de César baseadas em letras de uma senha. Trata-se de uma versão simplificada de uma mais geral cifra de substituição polialfabética, inventada por Leon Battista Alberti cerca de 1465.
(WIKIPEDIA, 2019)

## USO

>Python file system cipher.. vigenere [-h] -k KEY
                                        (-c CRYPT | -d DECRYPT)
                                                                                           
```
optional arguments:
  -h, --help            mostra as opções de linha de comando
  -c CRYPT, --crypt CRYPT
                        palavra a ser criptografada
  -d DECRYPT, --decrypt DECRYPT
                        palavra a ser descriptografada  
  -k KEY, --key KEY     especifica a palavra-chave
```

## EXEMPLOS
### Criptografar a palavra  "maj arthur gibson"

```
python vigenere.py  -k "WHITE STREET" -c "maj arthur gibson"

Resultado:

>> IHRTVSZNIKMUOVV

```

### Descriptografar a palavra anterior
```
python vigenere.py  -k "WHITE STREET" -d "IHRTVSZNIKMUOVV"

Resultado:

>> MAJARTHURGIBSON
```
