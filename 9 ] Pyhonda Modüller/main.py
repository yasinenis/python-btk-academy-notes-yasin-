import mod

result = help(mod)      # modül hakkında bilgi...
print(result)

result = help(mod.func) # sadece func() fonks hakkında bilgi...
print(result)


result = mod.number        # modülde tanımladığımız number = 10 tanımı
print(result)

result = mod.numbers        # tanımladığımız numbers gelir
print(result)

result = mod.person['name']
print(result)

result = mod.person["age"]
print(result)

result = mod.func(10)       # modda tanımlanan func fonksiyonu gelir
print(10)

# mod modülündeki class dan bu sayfada bir obje tanımlayacağız
p = mod.Person() 
p.speak()         # modülde speak fonksiyonunu person classı altında tanımlamıştık