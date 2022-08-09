# pythonwebservisbaglantisi
Python ile webservisden veri almak.

<br>
İlk olarak cmd konsolunu açınız ve aşağıdaki kodları sırası ile giriniz.
<br>
py -m pip install --upgrade pip
<br>
py -m pip install zeep
<br>
İşlemler bittikten sonra;
<br>
py -m zeep https://www.w3schools.com/xml/tempconvert.asmx?wsdl yazarak w3schooldan örnek olarak almış olduğumuz webservisin içindeki servisleri görebiliriz.

<br>
py -m zeep https://www.w3schools.com/xml/tempconvert.asmx?wsdl yazdığımızda resimde görüldüğü üzere aşağıdaki sorgular gelecektir.
<br>
![image](https://user-images.githubusercontent.com/62428397/183638023-ddccfd76-c3fd-4984-9522-329c210f61cc.png)

<br>
Aşağı kısımlara gittiğimizde Operations kısmında CelsiusToFahrenheit şeklinde operasyon göreceksiniz. Yukarıdaki kodlarda da gördüğünüz üzere 
client = Client(wsdl='https://www.w3schools.com/xml/tempconvert.asmx?wsdl') cliente w3school'un wsdl linkini koyduktan sonra client.service.CelsiusToFahrenheit yazarak bu operasyona ulaşıyoruz.
<br>
Bu operasyonda ![image](https://user-images.githubusercontent.com/62428397/183638685-5f68ad60-de94-4b38-afc0-57abc1339648.png) görüldüğü üzere tek bir veri girişi istiyor. Zaten operasyonda adından da anlaşıldığı üzere ısı çevirme olduğu için örnek olarak 12 yazdık.

<br>
![image](https://user-images.githubusercontent.com/62428397/183638283-a09fc158-fe0e-4931-9966-82da247a0e20.png)

