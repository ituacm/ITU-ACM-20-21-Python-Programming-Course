letters = {'a':0, 'b': 1, 'c': 2,'d':3, 'e':4,'f':5,'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11,
           'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22,
           'x':23, 'y':24, 'z':25, " ":26}

message = "sifrelenecek olan string"
encrypted = []

for i in message:                     # i, burada message stringinin tüm harflerini dolaşıyor
     encrypted.append(letters[i])     # letters[i], dictionary'de i yerinde olan harf key'inin value'sunu döndürüyor

print(encrypted)

reverse_enc = ""
key_list = list(letters.keys())   # Key'lerin listesi. Gösterimi: ["a", "b", "c", ..., "z", " "]
val_list = list(letters.values()) # Value'ların listesi. Gösterimi: [0, 1, 2, ..., 26]

for i in encrypted:                             # i burada encrypted listesindeki tüm sayıları dolaşıyor
     reverse_enc += key_list[val_list.index(i)]

# sayının value listesinde indexini bulduk. key listesinde aynı indexte bu sayının dictionary'deki key'i
# var. bu key karakterini alıp boş stringin sonuna ekledik.

print(reverse_enc)