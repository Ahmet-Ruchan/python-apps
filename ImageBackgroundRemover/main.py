from rembg import remove

input_path = "cr7.jpg"
output_path = "output.png" #png olması gerekiyor

with open(input_path, 'rb') as i: #rb --> byte olarak read ediyor, okuyor
    with open(output_path, 'wb') as a: #wb --> byte olarak write edecek, yazacak
        input_file = i.read() #input-path'den okudu
        output_file = remove(input_file) #arka planı kaldırdı
        a.write(output_file) #output_file içine yazdı
